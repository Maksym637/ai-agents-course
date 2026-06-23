### Building RAG Collections

---

1. Building the RAG Collection:

```python
from chromadb import Client
from chromadb.config import Settings
from chromadb.utils import embedding_functions

def build_chroma_collection(chunks, collection_name="rag_collection"):
    model_name = 'sentence-transformers/all-MiniLM-L6-v2'
    embed_func = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)

    client = Client(Settings())
    collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=embed_func
    )

    texts = [c["text"] for c in chunks]
    ids = [f"chunk_{c['id']}_{c['chunk_id']}" for c in chunks]
    metadatas = [{"id": c["id"], "chunk_id": c["chunk_id"]} for c in chunks]

    collection.add(documents=texts, metadatas=metadatas, ids=ids)
    return collection

rag_collection = build_chroma_collection(chunked_data)
```

2. Retrieving Relevant Chunks and Constructing Prompts:

```python
def retrieve_top_chunks(query, collection, top_k=1):
    results = collection.query(query_texts=[query], n_results=top_k)

    return [
        {
            "chunk": results['documents'][0][i],
            "id": results['metadatas'][0][i]['id'],
            "distance": results['distances'][0][i]
        }
        for i in range(len(results['documents'][0]))
    ]

query = "What are my learning plans for SQL?"
retrieved_chunks = retrieve_top_chunks(query, rag_collection, top_k=2)
print(retrieved_chunks)
```

3. Function to build a prompt:

```python
def build_prompt(user_prompt, retrieved_chunks=[]):
    prompt = f"Question: {user_prompt}\nContext:\n"

    for rc in retrieved_chunks:
        prompt += f"- {rc['chunk']}\n"

    prompt += "Answer:"

    return prompt

prompt = build_prompt(query, retrieved_chunks)
print(prompt)

#
# Example output:
# Question: What are my learning plans for SQL?
# Context:
# - Review different types of SQL joins — especially LEFT and FULL OUTER joins.
# - ...
# Answer:
#
```

---
