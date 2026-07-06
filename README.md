# 🤖 AI Resume Assistant

An AI-powered Resume Assistant built using Streamlit, LangChain, HuggingFace Embeddings, ChromaDB, and Google Gemini.

The application allows users to upload a resume in PDF format and ask questions about the resume using Retrieval-Augmented Generation (RAG).

----------------------

## 📌 Features

- 📄 Upload Resume PDF
- ✂️ Extract Resume Text
- 🧩 Split Resume into Chunks
- 🧠 Generate Semantic Embeddings
- 🗄️ Store Embeddings in ChromaDB
- 🔍 Retrieve Relevant Resume Information
- 🤖 Generate AI Responses using Google Gemini
- 💬 Interactive Chat Interface

----------------------

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application Framework |
| LangChain | RAG Framework |
| HuggingFace | Text Embeddings |
| ChromaDB | Vector Database |
| Google Gemini | Large Language Model |
| PyPDF | PDF Text Extraction |

----------------------

## 🏗️ Architecture

```text
                 Resume PDF
                      │
                      ▼
               PDF Text Extraction
                      │
                      ▼
               Text Chunking
                      │
                      ▼
        HuggingFace Embeddings
                      │
                      ▼
            Chroma Vector Database
                      │
                      ▼
                Retriever (Top-K)
                      │
                      ▼
              Google Gemini LLM
                      │
                      ▼
              AI Generated Answer
```

----------------------

## 🚀 Installation

Follow the steps below to set up and run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/pavankumarnambaru65-ux/Resume-Chatbot.git
```

### 2️⃣ Navigate to Project Folder

```bash
cd Resume-Chatbot
```

### 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 4️⃣ Activate Virtual Environment

#### macOS/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

----------------------

## 🔑 Environment Variables

Create a `.env` file in the project root and add your Google Gemini API key.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

> **Note:** Never upload your `.env` file or API key to GitHub. The `.env` file is already included in `.gitignore`.

---------------------

## ▶️ Run the Application

Run the following command to start the Streamlit application.

```bash
streamlit run app.py
```

After running the application, open your browser and navigate to:

http://localhost:8501

--------------------

## 💬 Sample Questions

Try asking questions like:

- What are my technical skills?
- Summarize my resume.
- What projects have I worked on?
- How many years of experience do I have?
- What certifications do I have?
- Which programming languages do I know?
- What tools have I worked with?
- Tell me about my work experience.

-------------------------

## 👨‍💻 Author

**Pavan Kumar**

- GitHub: https://github.com/pavankumarnambaru65-ux
- LinkedIn: (https://www.linkedin.com/in/pavan-nambaru-plsqldeveloper/)

---------------------

## 📄 License

This project is licensed under the MIT License.

---------------------

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support motivates me to build more open-source AI projects.

