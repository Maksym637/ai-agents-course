### The chat loop

---

What is a chat loop? Think of texting a friend: you send a message, get a reply, and respond again. In programming, a chat loop lets a user and an AI assistant interact repeatedly.

---

Example:

```python
import os
from openai import OpenAI

def build_messages(user_input, history=None):
    with open('system_prompt.txt', 'r') as file:
        system_instruction = file.read().strip()

    messages = [{"role": "system", "content": system_instruction}]

    if history:
        for u, a in history:
            messages.append({"role": "user", "content": u})
            messages.append({"role": "assistant", "content": a})

    messages.append({"role": "user", "content": user_input})

    return messages

def get_completion(messages, model="gpt-4o", max_tokens=50, temperature=0.7):
    try:
        client = OpenAI()
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    try:
        print("OpenAI Chat Completions API - Dynamic Assistant Demo")
        print("=" * 40)

        history = []

        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ["quit", "exit"]:
                print("Assistant: Goodbye! It was nice chatting with you.")
                break
            if not user_input:
                print("Please provide a valid input.")
                continue

            messages = build_messages(user_input, history)
            response = get_completion(messages)

            print(f"User: {user_input}")
            print(f"Assistant: {response}")

            history.append((user_input, response))

    except ValueError as ve:
        print(f"Configuration Error: {ve}")
        print("Please set your OPENAI_API_KEY environment variable.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```

---
