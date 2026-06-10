### General information

---

The basic example of using the `openai` module for model interaction is the following:

```python
from openai import OpenAI

client = OpenAI()
messages = [
    {"role": "user", "content": "What is the capital of France?"}
]
completion = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    max_tokens=50
)
print(completion.choices[0].message.content.strip())  # Paris is the capital of France.
```

Each message has a role that determines its purpose in the conversation:

- `system`: Sets instructions or context for the assistant (e.g., "You are a helpful assistant.");
- `user`: Represents input from the end user (e.g., a question or command);
- `assistant`: Represents responses from the AI assistant;

---
