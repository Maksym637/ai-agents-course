### Completion parameters

---

The most common parameters:

- temperature: Controls randomness and creativity.
- max_tokens: Limits response length.
- top_p: Another way to control randomness.
- n: Number of completions to generate.

---

More about **temperature**:

- **Low temperature (e.g., 0.2):** Output is focused and predictable.
- **High temperature (e.g., 1.0):** Output is more diverse and creative.

---

More about **max_tokens**:

The `max_tokens` parameter sets the maximum length of the model’s response. A token is about a word or a few characters. Use `max_tokens` to keep responses short or allow longer outputs. For example, to get a brief answer, set `max_tokens=20`. For more detail, use `max_tokens=100` or higher.

---
