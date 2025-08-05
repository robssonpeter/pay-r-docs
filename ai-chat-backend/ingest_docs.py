from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

# === Step 1: Load Markdown Files ===
print("🔍 Loading markdown documents...")
loader = DirectoryLoader(
    "./docs",
    glob="**/*.md",
    show_progress=True
)
documents = loader.load()
print(f"✅ Loaded {len(documents)} documents.")

# === Step 2: Split into Chunks ===
print("✂️ Splitting documents into chunks...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)
print(f"✅ Created {len(chunks)} text chunks.")

# === Step 3: Generate Embeddings ===
print("🧠 Creating embeddings with HuggingFace...")
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# === Step 4: Create FAISS Vector Store ===
print("💾 Saving vector store to ./vectorstore...")
vectorstore = FAISS.from_documents(chunks, embedding_model)
vectorstore.save_local("./vectorstore")

print("🎉 Done! Documentation is indexed and ready.")
