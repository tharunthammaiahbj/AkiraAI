import os
import json
from bs4 import BeautifulSoup
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

# Initialize the Gemini model
model = GenerativeModel("gemini-1.5-flash-002")

# Function to extract and process product details from HTML
def extract_product_details_from_html(html_file_path, output_json_path):
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Extract the relevant content (can be customized)
    text_content = html_content
    
    # Generate prompt dynamically for extracting product details
    prompt = f"""
    Extract all product details from the following HTML content. Provide the details in JSON format with keys like:
    - "product_name"
    - "price"
    - "description"
    - "image_url"
    - "availability"
    - "ratings"

    The JSON should be well-formatted with each product on a new line and properly indented.

    HTML content:
    {text_content}  # Limit content to avoid token overflow
    """

    # Send the prompt to the model
    response = model.generate_content([prompt])
    
    product_data = response.text
    # Parse the model's response
    # Save the extracted data to a JSON file
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(product_data, json_file, indent=4, ensure_ascii=False)
    
    print(f"Product details have been saved to {output_json_path}")

# Specify the input HTML file and output JSON file
html_file_path = "/workspaces/AkiraAI/scraped_content.html"  # Replace with your HTML file path
output_json_path = "output.json"

# Extract product details and save them to the JSON file
extract_product_details_from_html(html_file_path, output_json_path)
