# 📚 Academic Research Assistant using Multi-Document RAG

An AI-powered Academic Research Assistant built using **Retrieval-Augmented Generation (RAG)** for analyzing multiple research papers related to **AI in Healthcare**.
The system allows users to upload or process research papers and ask context-aware questions to receive summarized and accurate responses.

---

# 🚀 Features

* Multi-document research paper analysis
* Semantic search using vector embeddings
* Context-aware question answering
* Retrieval-Augmented Generation (RAG)
* Interactive ChatGPT-like UI using Streamlit
* Research methodology comparison
* Research gap identification

---

# 🛠️ Technologies Used

* Python
* Streamlit
* LangChain
* ChromaDB
* Hugging Face Embeddings
* Groq API
* PyPDF
* Sentence Transformers

---

# 📂 Project Structure

```bash
Mini_Project/
│
├── data/                     # Research papers (PDF/Text)
├── streamlit_app.py          # Main Streamlit application
├── requirements.txt          # Required libraries
├── .env                      # API key configuration
└── README.md                 # Project documentation
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your-github-repo-link>
cd Mini_Project
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

OR

```bash
pip install streamlit langchain langchain-community langchain-core langchain-huggingface langchain-groq langchain-chroma chromadb sentence-transformers pypdf python-dotenv
```

---

# 🔑 Environment Variables

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_api_key_here
```

Get API key from:
https://console.groq.com

---

# ▶️ Run the Project

```bash
python -m streamlit run streamlit_app.py
```

Open browser:

```bash
http://localhost:8501
```

---

# 💡 Sample Queries

* Compare methodologies used in the research papers
* Summarize findings from uploaded papers
* Identify research gaps in AI healthcare
* What machine learning models are used?

---

# 📊 System Workflow

1. Load research papers
2. Split documents into chunks
3. Generate embeddings
4. Store vectors in ChromaDB
5. Retrieve relevant content
6. Generate response using LLM

---

# 📌 Advantages

* Reduces manual literature review effort
* Provides accurate and context-aware answers
* Supports multi-document analysis
* User-friendly interface

---

# 🔮 Future Scope

* Real-time research database integration
* Multilingual support
* Advanced analytics dashboard
* Voice-based interaction

---

# 👩‍💻 Author

Project developed as part of mini project work on AI-powered academic research assistance.

---
