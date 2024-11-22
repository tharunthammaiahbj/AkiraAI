import os
from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel

# Load the environment variables from the .env file
load_dotenv()

# Retrieve the path to the JSON service file from .env
json_key_file_path = os.getenv("GOOGLE_CLOUD_AI_CREDENTIALS")

# Set the GOOGLE_CLOUD_AI_CREDENTIALS environment variable for authentication
os.environ["GOOGLE_CLOUD_AI_CREDENTIALS"] = json_key_file_path

# Initialize Vertex AI with the project ID (it will use the credentials from the environment variable)
vertexai.init(location="us-central1")

# Define the text prompt for text generation
text_prompt = "Write a creative story about a young explorer discovering a hidden city in the jungle."

# Initialize the model for text generation
model = GenerativeModel("gemini-1.5-flash-002")

# Generate text content based on the provided text prompt
response = model.generate_content([text_prompt])

# Output the generated response text
print(response.text)
