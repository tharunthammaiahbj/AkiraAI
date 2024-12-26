from transformers import AutoTokenizer

def calculate_tokens(html_content:str, model_id: str) -> int:
    
    """
    Calculate the number of tokens in the input text for the given model.

    Args:
        text (str): The input text to tokenize.
        model_id (str): The ID of the model (e.g., 'jinaai/reader-lm-0.5b').

    Returns:
        int: The number of tokens for the given text and model.
    """

    try:
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        tokens = tokenizer.encode(text=html_content)

        return len(tokens)
    
    except Exception as e:

        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    # Example usage
    text = "This is an example sentence to calculate token count."
    model_id = "jinaai/reader-lm-0.5b"  # Replace with your model ID
    
    token_count = calculate_tokens(text, model_id)
    print(f"Token count for the input text: {token_count}")


