import asyncio
import os
from akiraai.web_doc_loader.playwright_async_scraper import PlaywrightAsyncScraper

url_list = [
"https://www.airbnb.co.in/"
]

# Initialize the scraper
scraper = PlaywrightAsyncScraper(max_concurrency=3, timeout=30)

async def fetch_and_save_html():
    # Create a directory to store the HTML files
    os.makedirs("/workspaces/AkiraAI/Dataset/dataset_collection/raw_html/travel/airbnb", exist_ok=True)

    file_counter = 1  # Start the file naming with 1

    # Fetch URLs and handle the results
    async for doc in scraper.fetch_urls_with_browser(urls=url_list):
        html_content = doc.page_content

        if html_content:
            # Simple incremental filename
            filename = os.path.join("/workspaces/AkiraAI/Dataset/dataset_collection/raw_html/travel/airbnb", f"bnb_{file_counter}.html")
            file_counter += 1

            # Save the HTML content to the file
            with open(filename, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"Saved: {filename}")
        else:
            print(f"Failed to fetch content for one of the URLs.")

# Run the function
asyncio.run(fetch_and_save_html())
