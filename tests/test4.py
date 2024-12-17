import asyncio
from akiraai.web_doc_loader.playwright_async_scraper import PlaywrightAsyncScraper
from akiraai.utils.clean_up_html import reduce_html
from akiraai.utils.langchain_doc_converter import doc_converter

# Define test URLs
url_list = [
    "https://www.amazon.in/gp/bestsellers/automotive/5257482031/ref=zg_bs_nav_automotive_1"
]

# Initialize the scraper
scraper = PlaywrightAsyncScraper(max_concurrency=3, timeout=30)

# Define a function to fetch URLs and write the result to a file
async def test_scraper():
    # Call the async method that scrapes the URLs
    async for doc in scraper.fetch_urls_with_browser(urls=url_list):
        # For each document, print the URL and length of the cleaned HTML content
        print(f"Document URL: {doc.metadata['source']}")
        print(f"Title: {doc.metadata['title']}")
        print(f"Content Length: {len(doc.page_content)}")
        
        # Define the file name based on the URL or a static name
        output_file_name = "scraped_content.html"
        html_content = doc.page_content
        reduced_html = reduce_html(html=html_content, reduction=1)
                
        # Save the content to the file
        with open(output_file_name, 'w', encoding='utf-8') as file:
            file.write(reduced_html)
        
        print(f"Content saved to {output_file_name}")
        print('-' * 50)

# Run the test
asyncio.run(test_scraper())
