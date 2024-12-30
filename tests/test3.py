import asyncio
import os
from akiraai.web_doc_loader.playwright_async_scraper import PlaywrightAsyncScraper
from markdownify import markdownify as md 

url_list = [
    "https://sale.alibaba.com/p/rank/detail.html?spm=a27aq.rank_detail.6622646540.26.50c243bfiwWgnu&wx_navbar_transparent=true&cardType=101002747&cardId=10001239587&topOfferIds=&templateBusinessCode=&bucket=undefined"

]

# Initialize the scraper
scraper = PlaywrightAsyncScraper(max_concurrency=3, timeout=30)

async def test_scraper():
    # Create a directory to store the markdown files
    os.makedirs("/workspaces/AkiraAI/Dataset/Summarization/input_markdown/raw_markdown/e-commerce/alibaba", exist_ok=True)

    file_counter =10   # Start the file naming with 1

    # Fetch URLs and handle the results
    async for doc in scraper.fetch_urls_with_browser(urls=url_list):
        html_content = doc.page_content

        if html_content:
            # Convert HTML to markdown
            markdown_content = md(html_content)

            # Simple incremental filename
            filename = os.path.join("/workspaces/AkiraAI/Dataset/Summarization/input_markdown/raw_markdown/e-commerce/alibaba", f"ali_{file_counter}.md")
            file_counter += 1

            # Save the markdown content to the file
            with open(filename, "w", encoding="utf-8") as f:
                f.write(markdown_content)
            print(f"Saved: {filename}")
        else:
            print(f"Failed to fetch content for one of the URLs.")

# Run the test
asyncio.run(test_scraper())
