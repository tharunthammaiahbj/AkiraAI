from vertexai.preview.tokenization import get_tokenizer_for_model
import re

def count_tokens_gemini(html_content):

    tokenizer =get_tokenizer_for_model("gemini-1.5-flash-002")

    response = tokenizer.count_tokens(html_content)

    return response.total_tokens
    

with open("/workspaces/AkiraAI/scraped_content.html","r") as file:
    html_contents = file.read()

tokens = count_tokens_gemini(html_content=html_contents)

print(f"The number of tokens are : {tokens}")