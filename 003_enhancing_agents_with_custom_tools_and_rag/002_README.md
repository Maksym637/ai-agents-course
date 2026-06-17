## Chunking data

---

`Chunking` means dividing large text into smaller segments, or "chunks." Each chunk should be small enough for the AI to handle, but large enough to keep useful information.

Example:

```python
def chunk_text(text, chunk_size=30):
    """Split text into fixed-size chunks."""
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks


chunks = chunk_text(
    text="This is a sample document that we want to split into smaller chunks for easier processing.",
    chunk_size=20
)
print(chunks)
```

---

Practical Considerations:

- **Chunk size**: Pick a size that fits your AI model’s input limit. For many models, this is 200–500 words, but check your model’s documentation.
- **Chunk boundaries**: Split at natural points, like sentences or paragraphs, to keep meaning.
- **Overlapping chunks**: Sometimes, let chunks overlap a bit so important information at the edge of one chunk is also in the next. This helps preserve context.
- **Metadata**: Always track which chunk came from which document and its position. This is key for reconstructing answers or providing references.

---
