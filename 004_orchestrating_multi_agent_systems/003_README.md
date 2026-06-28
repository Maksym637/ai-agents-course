### Orchestrating workflows

---

The manager agent setup:

```python
from todo_agent import TODO_AGENT
from rag_agent import RAG_AGENT
from agents import Runner, Agent
from rag_builder import build_rag

MANAGER_AGENT = Agent(
    name="Manager Agent",
    instructions=(
        "You are a manager agent that orchestrates multiple agents. "
        "You can delegate tasks to the Todo Agent and the Learn Agent. "
        "Use the Todo Agent for task management and the Learn Agent for retrieving learning items and returning it to the user."
    ),
    tools=[
        TODO_AGENT.as_tool(
            tool_name="todo_agent",
            tool_description="A tool for managing tasks using the Todo API"
        ),
        RAG_AGENT.as_tool(
            tool_name="rag_agent",
            tool_description="A tool for providing answers regarding user's learning items"
        )
    ]
)
```

The orchestration loop:

```python
def run_manager_agent(requests):
    build_rag()

    input_index = 0
    while True:
        if input_index >= len(requests):
            print("No more user requests. Exiting the manager agent.")
            break

        user_input = requests[input_index]
        input_index += 1
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the manager agent.")
            break

        result = Runner.run_sync(MANAGER_AGENT, user_input)
        print(f"Manager Agent: {result.final_output}")
```

Execution of the `run_manager_agent` function:

```python
from manager import run_manager_agent

if __name__ == '__main__':
    user_inputs = [
        "List all my tasks",
        "Create a new task with title 'Learn Python' and description 'Complete the Python course'",
        "What are my learning plans for React",
        "exit"
    ]

    run_manager_agent(user_inputs)
```

---
