import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

# Load the API token from the .env file

with open("/workspaces/AkiraAI/scraped_content.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")
cleaned_content = soup.get_text(separator=" ", strip=True)


load_dotenv()
api_token = os.getenv("HF_API_KEY")

if not api_token:
    raise ValueError("HUGGING_FACE_API_TOKEN is not set in the .env file.")

model_id="jinaai/reader-lm-0.5b"

# API endpoint
api_url = f"https://api-inference.huggingface.co/models/{model_id}"

# Headers with the API token
headers = {"Authorization": f"Bearer {api_token}"}

# Input payload
payload = {
    "inputs": html_content,
    "parameters": {
        "max_length": 50,  # Adjust as needed
        "temperature": 0.7  # Adjust creativity
    }
}

# Send the POST request to the API
response = requests.post(api_url, headers=headers, json=payload)

# Process the response
# Process the response
if response.status_code == 200:
    generated_text = response.text  # Directly use the raw text response
    
    # Specify the output Markdown file
    output_md_file = "output.md"
    
    # Write the generated text to the Markdown file
    try:
        with open(output_md_file, "w", encoding="utf-8") as md_file:
            md_file.write(generated_text)
        print(f"Generated Markdown content successfully written to {output_md_file}.")
    except Exception as e:
        print(f"An error occurred while writing to the Markdown file: {e}")
else:
    print(f"Error {response.status_code}: {response.text}")

