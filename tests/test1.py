import os
import requests
import time
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

# Prepare the output content by processing the chunks
generated_markdown = ""

# Process each chunk
for i, chunk in enumerate(html_chunks):
    print(f"Processing chunk {i + 1}/{len(html_chunks)}...")  # Log which chunk is being processed
    
    # Prepare the payload for the request
    payload = {
        "inputs": chunk
    }
    
    # Retry mechanism in case of failure
    retries = 3
    for attempt in range(retries):
        try:
            # Send the POST request to the API
            response = requests.post(api_url, headers=headers, json=payload)
            
            # Check if the request was successful
            if response.status_code == 200:
                generated_text = response.text  # Directly use the raw text response
                print(f"Generated text for chunk {i + 1}: {generated_text}")  # Output the generated text directly
                generated_markdown += generated_text  # Append to the result
                break  # Break the retry loop if successful
            else:
                print(f"Error {response.status_code}: {response.text}")
                raise Exception("Request failed, retrying...")

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {str(e)}")
            # Wait before retrying the request to avoid hitting rate limits or overwhelming the server
            time.sleep(2 ** attempt)  # Exponential backoff
        
    else:
        print(f"All attempts failed for chunk {i + 1}, skipping...")

# Write the generated content to the Markdown file (just in case)
output_md_file = "output.md"
try:
    with open(output_md_file, "w", encoding="utf-8") as md_file:
        md_file.write(generated_markdown)
    print(f"Generated Markdown content successfully written to {output_md_file}.")
except Exception as e:
    print(f"An error occurred while writing to the Markdown file: {e}")
