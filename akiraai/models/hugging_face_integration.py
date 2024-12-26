import os
import requests
from dotenv import load_dotenv
from akiraai.utils.text_to_chunks import chunk_html_by_tokens

# Load the API token from the .env file
load_dotenv()
api_token = os.getenv("HF_API_KEY")

if not api_token:
    raise ValueError("HUGGING_FACE_API_TOKEN is not set in the .env file.")

# Read the HTML content from the file
with open("/workspaces/AkiraAI/scraped_content.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Define the model ID and API endpoint
model_id = "jinaai/reader-lm-0.5b"
api_url = f"https://api-inference.huggingface.co/models/{model_id}"

# Headers with the API token
headers = {"Authorization": f"Bearer {api_token}"}

# Split the cleaned content into chunks based on the token limit
max_tokens = 4096  # Adjust as necessary for the model
html_chunks = chunk_html_by_tokens(html_content, model_id, max_tokens)  # Assuming you have this function

# Prepare the output content by processing each chunk through the model
generated_markdown = ""

for chunk in html_chunks:
    payload = {
        "inputs": chunk,
        "parameters": {
            "max_length": 50,  # You can adjust this parameter based on the model's capabilities
            "temperature": 0.7  # Creativity of the model's output
        }
    }
    
    # Send the POST request to the API
    response = requests.post(api_url, headers=headers, json=payload)

    # Process the response
    if response.status_code == 200:
        generated_text = response.text  # Directly use the raw text response
        generated_markdown += generated_text  # Append to the Markdown output
    else:
        print(f"Error {response.status_code}: {response.text}")

# Write the generated content to the Markdown file
output_md_file = "output.md"
try:
    with open(output_md_file, "w", encoding="utf-8") as md_file:
        md_file.write(generated_markdown)
    print(f"Generated Markdown content successfully written to {output_md_file}.")
except Exception as e:
    print(f"An error occurred while writing to the Markdown file: {e}")
