from transformers import AutoTokenizer, AutoModel
import torch

def initialize_model_pool(model_path, pool_size=2, tokenizer_options=None, model_options=None):
    """
    Initialize a pool of models and tokenizers with optional configurations.

    Args:
        model_path (str): Path or name of the pretrained model.
        pool_size (int): Number of model instances in the pool. Defaults to 4.
        tokenizer_options (dict, optional): Additional options for initializing the tokenizer. Defaults to None.
        model_options (dict, optional): Additional options for initializing the model. Defaults to None.

    Returns:
        list: A list containing (tokenizer, model) pairs.
    """
    tokenizer_options = tokenizer_options or {}
    model_options = model_options or {}

    pool = []
    for _ in range(pool_size):
        tokenizer = AutoTokenizer.from_pretrained(model_path, **tokenizer_options)
        model = AutoModel.from_pretrained(model_path, **model_options)
        pool.append((tokenizer, model))
    
    return pool


def mean_pooling(model_output, attention_mask):
    """
    Perform mean pooling on the token embeddings based on the attention mask.

    Args:
        model_output (torch.Tensor): The output of the model.
        attention_mask (torch.Tensor): The attention mask.

    Returns:
        torch.Tensor: The result of mean pooling.
    """
    token_embeddings = model_output[0]  # (batch_size, seq_len, hidden_dim)
    input_mask_expanded = attention_mask.unsqueeze(-1).float()  # (batch_size, seq_len, 1)

    # Masked sum of embeddings
    sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, dim=1)  # (batch_size, hidden_dim)

    # Count of non-padding tokens
    sum_mask = input_mask_expanded.sum(dim=1).clamp(min=1e-9)  # (batch_size, 1)

    # Mean pooling
    return sum_embeddings / sum_mask







