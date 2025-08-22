

# My\_AI – Local RAG Chatbot using Ollama + ChromaDB + Gradio

This project is a **Retrieval-Augmented Generation (RAG) chatbot** built with:

* [Ollama](https://ollama.ai/) for running LLMs locally (e.g. `llama3`)
* [ChromaDB](https://docs.trychroma.com/) for document storage & retrieval
* [Gradio](https://www.gradio.app/) for a simple web UI

The chatbot answers user queries based on your **custom knowledge base**.

---

## 🚀 Features

* Run **Llama3** (or any Ollama model) locally without GPU requirement.
* Add your own documents to ChromaDB for retrieval.
* Simple **Gradio Web UI** to ask questions.
* Persistent storage of embeddings in local folder (`chroma_db/`).

---

## 📂 Project Structure

```
My_AI/
│── app.py          # Main Gradio app
│── abc.py          # Creates collection and inserts initial docs
│── rag.py          # Query handling logic
│── add_docs.py     # (Optional) Script to add more docs
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1. Clone Repo

```bash
git clone https://github.com/<your-username>/My_AI.git
cd My_AI
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt` should include:

```
chromadb
gradio
ollama
```

### 3. Install Ollama

Download Ollama from [here](https://ollama.ai/download) and make sure it is running in background.

Verify installation:

```bash
ollama run llama3
```

---

## 📥 Load Knowledge Base

Run the script to create a persistent ChromaDB collection and insert sample docs:

```bash
python abc.py
```

You should see:

```
Collection 'knowledge_base' created and documents inserted ✅
```

---

## ▶️ Run the App

Start the chatbot:

```bash
python app.py
```

Open browser at:

```
http://127.0.0.1:7860
```

Ask:

```
Who is CM of Bihar?
```

Output:

```
Nitish Kumar is the Chief Minister of Bihar in 2025.
```

---

## ➕ Adding More Documents

To add more knowledge later, create a file `add_docs.py` like:

```python
import chromadb

client = chromadb.PersistentClient(path="D:/Desktop/My_AI/chroma_db")
collection = client.get_or_create_collection("knowledge_base")

collection.add(
    documents=["Visteon is a global automotive electronics company."],
    ids=["doc4"]
)

print("New document added ✅")
```

Run:

```bash
python add_docs.py
```

---

## 📌 Notes

* Knowledge base is **local only** (stored in `chroma_db/`).
* No internet queries are done – only your documents are used.
* Ollama should always be running before launching `app.py`.

---

## 🛠 Future Improvements

* Upload PDFs and auto-ingest into ChromaDB
* Use embeddings models instead of plain text retrieval
* Add authentication for web UI

---

## 📝 License

MIT License.

---

