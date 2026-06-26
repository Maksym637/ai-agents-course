### Enhancing a TODO API Agent

---

The entire implementation but with all CRUD operations:

1. Models definition:

```python
from pydantic import BaseModel

class TodoItem(BaseModel):
    id: int
    title: str
    done: bool
    description: str
```

```python
from enum import Enum
from typing import Optional

class Action(str, Enum):
    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"
```

```python
class TodoItemArgs(BaseModel):
    action: Action
    task: Optional[TodoItem] = None
```

2. Implementing CRUD in the TodoAPI Class:

```python
@classmethod
def get_tasks(cls):
    response = requests.get(cls.BASE_URL)
    response.raise_for_status()
    return [TodoItem(**item) for item in response.json()]
```

```python
@classmethod
def create_task(cls, task: TodoItem):
    response = requests.post(cls.BASE_URL, json=task.dict())
    response.raise_for_status()
    return TodoItem(**response.json())
```

```python
@classmethod
def update_task(cls, task: TodoItem):
    response = requests.put(f"{cls.BASE_URL}/{task.id}", json=task.dict())
    response.raise_for_status()
    return TodoItem(**response.json())
```

```python
@classmethod
def delete_task(cls, task: TodoItem):
    response = requests.delete(f"{cls.BASE_URL}/{task.id}")
    response.raise_for_status()
    return {"message": "Task deleted successfully"}
```

```python
@classmethod
def handle_request(cls, action, task):
    if action == Action.GET:
        tasks = cls.get_tasks()
        return [t.dict() for t in tasks]
    elif action == Action.POST:
        return cls.create_task(task).dict()
    elif action == Action.PUT:
        return cls.update_task(task).dict()
    elif action == Action.DELETE:
        return cls.delete_task(task)
    else:
        raise ValueError(f"Unknown action: {action}")
```

3. Integrating CRUD with the Agent:

```python
todos_api_tool = FunctionTool(
    name="todos_api",
    description="A tool for interacting with the Todo API",
    params_json_schema=model_json_schema,
    on_invoke_tool=run_function
)
```

```python
TODO_AGENT = Agent(
    name="Todo Manager",
    instructions=(
        "You are a Todo API agent. "
        "You can create, read, update, and delete tasks using the Todo API. "
        "Use the todos_api tool to interact with the API. "
        "For GET and PUT actions: always first list all tasks (use GET), then proceed with the requested operation (for PUT, update the task after listing). "
        "For DELETE action: you must first list all the tasks, identify the ID of the task you need to remove and then use the tool to delete the task."
    ),
    tools=[todos_api_tool]
)
```

4. Example Interactions:

- Create a new task:

```python
query = "Create a new task with title 'Learn Python' and description 'Complete the Python course'"
response = ask_agent(query)
```

- Delete a task:

```python
query = "Delete the python learning task"
response = ask_agent(query)
```

---
