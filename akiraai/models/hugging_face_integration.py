import os
import requests
from dotenv import load_dotenv

# Load the API token from the .env file
load_dotenv()
api_token = os.getenv("HF_API_KEY")

if not api_token:
    raise ValueError("HUGGING_FACE_API_KEY is not set in the .env file.")

# Read the Markdown content from the file
with open("/workspaces/AkiraAI/Dataset/dataset_collection/raw_markdown/e-commerce/amazon/zon_2.md", "r", encoding="utf-8") as file:
    markdown_content = file.read()

# Define the model ID and API endpoint
model_id = "meta-llama/Llama-3.2-1B-Instruct"
api_url = f"https://api-inference.huggingface.co/models/{model_id}"

# Headers with the API token
headers = {"Authorization": f"Bearer {api_token}"}

# Prepare a prompt that instructs the model to extract product information
prompt = f"Extract product information from the following content:\n\n{markdown_content}\n\nProduct Information:"

payload = {
    "inputs": prompt,
    "parameters": {
        "max_length": 4096,  # Adjust based on expected output length
        "temperature": 0.7   # Adjust for creativity of output
    }
}

# Send the POST request to the API
response = requests.post(api_url, headers=headers, json=payload)

# Process the response
if response.status_code == 200:
    generated_text = response.json().get("generated_text", "")  # Use JSON response for better handling
    print("Generated Product Information:")
    print(generated_text)  # Print or further process the generated text
else:
    print(f"Error {response.status_code}: {response.text}")

# Optionally, write the generated content to a Markdown file
output_md_file = "output.md"
try:
    with open(output_md_file, "w", encoding="utf-8") as md_file:
        md_file.write(generated_text)
    print(f"Generated Markdown content successfully written to {output_md_file}.")
except Exception as e:
    print(f"An error occurred while writing to the Markdown file: {e}")
