### Designing a TODO Agent

---

Key components:

- **Agent:** Receives user prompts and decides what to do.
- **Tool:** Wraps specific functionality (like calling an API) for the agent.
- **API Interaction:** Handles communication with the external `Todo API`.

---

### Step by step guide

1. Defining Actions and Data Models:

```python
from enum import Enum

class Action(Enum):
    GET = "get"
```

```python
from pydantic import BaseModel

class TodoItem(BaseModel):
    id: int
    title: str
    done: bool
    description: str
```

```python
class TodoItemArgs(BaseModel):
    action: Action
```

2. Implementing the TodoAPI Class:

```python
import requests
import json

class TodoAPI:
    BASE_URL = "http://127.0.0.1:8000/todos"

    @classmethod
    def get_tasks(cls):
        response = requests.get(cls.BASE_URL)
        response.raise_for_status()
        return [TodoItem(**item) for item in response.json()]

    @classmethod
    def handle_request(cls, action):
        if action == Action.GET:
            tasks = cls.get_tasks()
            tasks_dicts = [task.dict() for task in tasks]
            return tasks_dicts
        else:
            raise ValueError(f"Unknown action: {action}")

async def run_function(ctx: RunContextWrapper[Any], args: str) -> str:
    parsed = TodoItemArgs.model_validate_json(args)
    return json.dumps({"tasks": TodoAPI.handle_request(parsed.action)})
```

3. Integrating the API with the Agent: Creating the Tool:

```python
from agents import FunctionTool

todos_api_tool = FunctionTool(
    name="todos_api",
    description="A tool for interacting with the Todo API",
    params_json_schema = {
        **TodoItemArgs.model_json_schema(),
        "additionalProperties": False
    },
    on_invoke_tool=run_function
)
```

4. Integrating the API with the Agent: Defining the Agent:

```python
from agents import Agent

TODO_AGENT = Agent(
    name="Todo Manager",
    instructions=(
        "You are a Todo API agent. "
        "You can read tasks using the Todo API."
        "Use the todos_api tool to interact with the API."
    ),
    tools=[todos_api_tool]
)
```

5. Using the Agent in Practice:

```python
from todo_agent import ask_agent

def main():
    query = "Hey list all my tasks"
    response = ask_agent(query)
    print(response)
    # response = [
    #     {
    #         "id": 1,
    #         "title": "Buy milk",
    #         "done": False,
    #         "description": "Get 2 liters of milk",
    #     },
    #     {
    #         "id": 2,
    #         "title": "Read book",
    #         "done": True,
    #         "description": "Finish reading 'Atomic Habits'",
    #     },
    # ]

if __name__ == '__main__':
    main()
```

---
