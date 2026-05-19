import os
import streamlit as st
from dotenv import load_dotenv

# LangChain Imports
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

# Load API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Research Assistant", page_icon="📚")
st.title("📚 Academic Research Assistant")

# -------------------------------
# LOAD DATA (cached)
# -------------------------------
@st.cache_resource
def load_data():
    DATA_PATH = "data"
    documents = []

    for file in os.listdir("data"):
        path = os.path.join("data", file)

        if file.endswith(".pdf"):
            docs = PyPDFLoader(path).load()
            for d in docs:
                d.metadata["source"] = file
            documents.extend(docs)


    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = Chroma.from_documents(chunks, embeddings)
    retriever = vector_db.as_retriever(search_kwargs={"k": 8})


    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model="llama-3.1-8b-instant"
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system",
         """You are an Academic Research Assistant.

    STRICT INSTRUCTIONS:
    - Answer ONLY using the provided context.
    - ALWAYS mention the source paper name.
    - Cite like: (Source: paper_name.pdf)
    - Do NOT give generic answers.

    Tasks:
    1. Identify methodologies
    2. Compare them
    3. Mention which paper uses which method

    Context:
    {context}
    """),
        ("human", "{input}")
    ])



    qa_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, qa_chain)

    return rag_chain

rag_chain = load_data()

# -------------------------------
# CHAT HISTORY
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -------------------------------
# USER INPUT
# -------------------------------
if prompt := st.chat_input("Ask about your research papers..."):

    # Show user message
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # 🔥 Get response FIRST
    response = rag_chain.invoke({"input": prompt})

    answer = response.get("answer", "")

    st.write(answer)

    # 🔥 Show sources
    sources = set()
    for doc in response.get("context", []):
        if "source" in doc.metadata:
            sources.add(doc.metadata["source"])

    if sources:
        st.write("### 📄 Sources:")
        for s in sources:
            st.write("-", s)
