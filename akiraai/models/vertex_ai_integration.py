import os
import json
from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel

# Load the environment variables from the .env file
load_dotenv()

# Retrieve the path to the JSON service file from the .env file
json_key_file_path = os.getenv("GOOGLE_CLOUD_AI_CREDENTIALS")
if not json_key_file_path:
    raise ValueError("Environment variable GOOGLE_CLOUD_AI_CREDENTIALS is not set")

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_key_file_path

# Read the JSON file and extract the project_id
with open(json_key_file_path, 'r') as file:
    service_account_data = json.load(file)
    project_id = service_account_data.get("project_id")
    if not project_id:
        raise ValueError("Project ID not found in the service account JSON file")

# Initialize Vertex AI with the project ID
vertexai.init(location="us-central1", project=project_id)

# Define the text prompt for text generation
text_prompt = "Write a creative story about a young explorer discovering a hidden city in the jungle."

# Initialize the model for text generation
model = GenerativeModel("gemini-1.5-flash-002")

# Generate text content based on the provided text prompt
response = model.generate_content([text_prompt])

# Output the generated response text
print(response.text)