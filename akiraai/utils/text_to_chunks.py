from transformers import AutoTokenizer
from typing import List

def chunk_html_by_tokens(html_content: str, model_id: str, max_tokens: int) -> List[str]:
    """
    Chunk raw HTML content into smaller parts within the model's max token limit.
    
    Args:
        html_content (str): The raw HTML content.
        model_id (str): The model ID to use for tokenization.
        max_tokens (int): Maximum tokens allowed per chunk.

    Returns:
        List[str]: A list of HTML chunks, each within the token limit (including buffer).
    """
    # Adjust max tokens to include a 500-token buffer
    effective_max_tokens = max_tokens - 500

    # Initialize the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    # Tokenize the entire content
    total_tokens = tokenizer.encode(html_content, add_special_tokens=False)
    total_token_count = len(total_tokens)

    # If the total tokens are within the max limit, return as a single chunk
    if total_token_count <= effective_max_tokens:
        return [html_content]

    # Split into chunks
    chunks = []
    current_start = 0

    while current_start < total_token_count:
        # Calculate end position for this chunk
        current_end = min(current_start + effective_max_tokens, total_token_count)

        # Decode back into a chunk of text
        chunk_tokens = total_tokens[current_start:current_end]
        chunk_text = tokenizer.decode(chunk_tokens, skip_special_tokens=True)

        chunks.append(chunk_text)
        current_start = current_end

    return chunks

# Example Usage
with open("/workspaces/AkiraAI/scraped_content.html", "r", encoding="utf-8") as file:
    html_content = file.read()

model_id = "jinaai/reader-lm-0.5b"
max_tokens = 4096
html_chunks = chunk_html_by_tokens(html_content, model_id, max_tokens)

print(f"Generated {len(html_chunks)} chunks.")

# Add token count verification for each chunk
tokenizer = AutoTokenizer.from_pretrained(model_id)  # Initialize tokenizer outside the loop for efficiency
for i, chunk in enumerate(html_chunks):
    token_count = len(tokenizer.encode(chunk, add_special_tokens=False))
    print(f"Chunk {i+1} token count: {token_count}")
