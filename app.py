import os
import streamlit as st

from dotenv import load_dotenv
from pypdf import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI

# ---------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ---------------------------------------------------
# Streamlit Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="🤖 Alexa 2.0",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Alexa 2.0")

st.markdown("### Upload your Resume and chat with AI")

# ---------------------------------------------------
# Session State
# ---------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "llm" not in st.session_state:
    st.session_state.llm = None

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.header("Resume Upload")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------------------------------------------
# Process Resume
# ---------------------------------------------------

if uploaded_file:

    st.success("✅ Resume Uploaded Successfully")

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    st.subheader("📄 Resume Preview")

    st.write(text[:1000])

    # ----------------------------------------------

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=500,

        chunk_overlap=100

    )

    chunks = splitter.split_text(text)

    st.success(f"✅ Total Chunks : {len(chunks)}")

    # ----------------------------------------------

    embeddings = HuggingFaceEmbeddings(

        model_name="sentence-transformers/all-MiniLM-L6-v2"

    )

    st.success("✅ Embeddings Created")

    # ----------------------------------------------

    vector_db = Chroma.from_texts(

        texts=chunks,

        embedding=embeddings,

        persist_directory="chroma_db"

    )

    st.success("✅ Vector Database Ready")

    retriever = vector_db.as_retriever(

        search_kwargs={"k":3}

    )

    st.session_state.retriever = retriever

    llm = ChatGoogleGenerativeAI(

        model="gemini-2.5-flash",

        google_api_key=GOOGLE_API_KEY,

        temperature=0.3

    )

    st.session_state.llm = llm

    st.success("✅ Gemini Loaded")

# ---------------------------------------------------
# Display Chat History
# ---------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ---------------------------------------------------
# Chat Input
# ---------------------------------------------------

question = st.chat_input("Ask anything about the uploaded resume...")

if question:

    # Display User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # Check Resume Uploaded

    if st.session_state.retriever is None:

        answer = "⚠️ Please upload a resume first."

    else:

        docs = st.session_state.retriever.invoke(question)

        context = ""

        for doc in docs:

            context += doc.page_content + "\n\n"

        prompt = f"""
You are an AI Resume Assistant.

Answer ONLY from the resume context.

If the answer is not available in the resume,
reply:

"I couldn't find that information in the uploaded resume."

Resume Context:

{context}

User Question:

{question}
"""

        response = st.session_state.llm.invoke(prompt)

        answer = response.content

    # Display Assistant Message

    with st.chat_message("assistant"):

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )        