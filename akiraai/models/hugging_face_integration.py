import os
import requests
from dotenv import load_dotenv

# Load the API token from the .env file
load_dotenv()
api_token = os.getenv("HF_API_KEY")

if not api_token:
    raise ValueError("HUGGING_FACE_API_TOKEN is not set in the .env file.")

model_id="google/flan-t5-large"

# API endpoint
api_url = f"https://api-inference.huggingface.co/models/{model_id}"

# Headers with the API token
headers = {"Authorization": f"Bearer {api_token}"}

# Input payload
payload = {
    "inputs": "Explain the concept of neural networks in simple terms.",
    "parameters": {
        "max_length": 50,  # Adjust as needed
        "temperature": 0.7  # Adjust creativity
    }
}

# Send the POST request to the API
response = requests.post(api_url, headers=headers, json=payload)

# Process the response
if response.status_code == 200:
    output = response.json()
    print("Generated Output:", output[0]["generated_text"])
else:
    print(f"Error {response.status_code}: {response.text}")
