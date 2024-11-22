import os
import json
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Retrieve the path to the JSON service account file from the .env file
json_key_file_path = os.getenv("GOOGLE_CLOUD_AI_CREDENTIALS")

# Read the JSON file and extract the project_id
with open(json_key_file_path, 'r') as file:
    service_account_data = json.load(file)
    project_id = service_account_data.get("project_id")

# Output the extracted project_id
print(f"Project ID: {project_id}")
