### Agents as Tools

---

- **Modularity**: Each agent focuses on one job, making code easier to manage.
- **Reusability**: Specialized agents can be reused in different projects.
- **Separation of Concerns**: Agents can be developed and tested independently.

---

An Orchestrator Agent

```python
from agents import Agent

orchestrator = Agent(
    name="Orchestrator",
    # Agents wrapped as tools
    tools=[web_search_tool, file_read_tool],
    instructions=(
        "You are an orchestrator agent. Use the web search tool to find information on the web "
        "and the file read tool to read the content of a file."
    )
)
```

---
