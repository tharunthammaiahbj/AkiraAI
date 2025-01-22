from transformers import AutoTokenizer, AutoModel
import torch

def initialize_embedding_model():
    """
    Initializes the embedding model by loading the tokenizer and model from a local directory.
    Returns the initialized tokenizer and model.
    """
    local_model_path = "/workspaces/AkiraAI/akiraai/models/minilm-v6-local"  # Replace with the actual path
    tokenizer = AutoTokenizer.from_pretrained(local_model_path)
    model = AutoModel.from_pretrained(local_model_path)
    return tokenizer, model

def mean_pooling(self, model_output, attention_mask):
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


