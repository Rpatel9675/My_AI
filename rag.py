import chromadb

client = chromadb.PersistentClient(path="D:/Desktop/My_AI/chroma_db")

def rag_query(query_text: str):
    try:
        collection = client.get_collection("knowledge_base")
    except:
        return "❌ Collection 'knowledge_base' not found. Run abc.py first."

    results = collection.query(
        query_texts=[query_text],
        n_results=3
    )
    return results
