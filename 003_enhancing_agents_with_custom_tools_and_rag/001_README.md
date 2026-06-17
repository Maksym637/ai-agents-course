### RAG general information

---

**Retrieval-Augmented Generation (RAG)** helps AI agents find and use relevant information from a knowledge base for more accurate answers. By the end, you’ll know how to create a basic agent that uses RAG to answer user queries more effectively.

---

Simple RAG Retrieval Logic:

```python
def rag_retrieval(query, knowledge_base):
    query_words = set(query.lower().split())
    best_doc = None
    best_overlap = 0
    for doc in knowledge_base:
        doc_words = set(doc["content"].lower().split())
        overlap = len(query_words & doc_words)
        if overlap > best_overlap:
            best_overlap = overlap
            best_doc = doc
    return best_doc if best_overlap > 0 else None


query = "How should I start tackling React useContext"
best_doc = rag_retrieval(query, data)
print(best_doc)  # {'id': 2, 'content': "Experiment with React's useContext by creating a theme toggler component."}
```

---
