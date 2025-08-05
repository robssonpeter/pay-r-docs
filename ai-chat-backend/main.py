from fastapi import FastAPI
from pydantic import BaseModel
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

app = FastAPI()

# === Step 1: Load FAISS Vector Store ===
print("🔍 Loading vector store...")
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("./vectorstore", embeddings=embedding_model, allow_dangerous_deserialization=True)

retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# === Step 2: Set Up Local LLM via Ollama ===
print("🧠 Connecting to local LLM (Ollama)...")
llm = Ollama(model="mistral")  # You can change to "llama3", "openhermes", etc.

# === Step 3: Build the Retrieval QA Chain ===
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=False
)

# === Step 4: Define Request/Response Format ===
class Question(BaseModel):
    message: str

@app.post("/ask")
async def ask(question: Question):
    print(f"📩 Question received: {question.message}")
    try:
        answer = qa_chain.run(question.message)
        return {"reply": answer}
    except Exception as e:
        return {"reply": f"❌ Error: {str(e)}"}
