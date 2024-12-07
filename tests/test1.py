import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv("SCRAPE_DO_TOKEN")


print(f"Token: {token}")