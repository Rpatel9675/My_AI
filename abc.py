import chromadb

# Persistent DB ek fixed folder me rakho
client = chromadb.PersistentClient(path="D:/Desktop/My_AI/chroma_db")

collection = client.get_or_create_collection(
    name="knowledge_base",
    metadata={"hnsw:space": "cosine"}
)

# Kuch sample docs daal dete hain
documents = [
    "Nitish Kumar is the Chief Minister of Bihar in 2025.",
    "Bihar is a state in eastern India.",
    "Patna is the capital city of Bihar."
]

collection.add(
    documents=documents,
    ids=["doc1", "doc2", "doc3"]
)

print("Collection 'knowledge_base' created and documents inserted ✅")
