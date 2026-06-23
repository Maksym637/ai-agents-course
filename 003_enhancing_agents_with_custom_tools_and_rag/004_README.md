### Custom RAG Retrieval Tool

---

Integrating the Tool with the Agent:

```python
from agents import Agent

AGENT = Agent(
    name="Learning Assistant",
    instructions=(
        "You are a personal learning assistant with access to rag tool. "
        "Whenever asked a question about learning plans, use the RAG retrieval tool to get context from the DB and answer user questions."
    ),
    tools=[rag_retrieval_tool] # RAG as a tool
)
```

---
