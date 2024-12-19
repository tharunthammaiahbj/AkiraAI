import asyncio
from akiraai.web_doc_loader.playwright_async_scraper import PlaywrightAsyncScraper

url_list = [
    "https://en.wikipedia.org/wiki/Deaths_in_2024",
    "https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers",
    "https://www.amazon.in/gp/bestsellers/automotive/ref=zg_bs_nav_automotive_0",
    "https://www.amazon.in/gp/bestsellers/automotive/5257482031/ref=zg_bs_nav_automotive_1",
    "https://www.amazon.in/gp/bestsellers/automotive/5257605031/ref=zg_bs_nav_automotive_2_5257482031",
    "https://www.amazon.in/gp/bestsellers/automotive/5257477031/ref=zg_bs_nav_automotive_1",
    "https://www.amazon.in/gp/bestsellers/automotive/5257556031/ref=zg_bs_nav_automotive_2_5257477031",
    "https://www.amazon.in/gp/bestsellers/automotive/51396100031/ref=zg_bs_nav_automotive_2_5257556031",
    "https://www.amazon.in/gp/bestsellers/gift-cards/92070982031/ref=zg_bs_nav_gift-cards_1",
    "https://www.amazon.in/gp/bestsellers/gift-cards/92070985031/ref=zg_bs_nav_gift-cards_1_92070982031"
]

# Initialize the scraper
scraper = PlaywrightAsyncScraper(max_concurrency=3, timeout=30)

async def test_scraper():
    # Fetch URLs and handle the results
    async for doc in scraper.fetch_urls_with_browser(urls=url_list):
        url = doc.metadata.get("source")
        html_content = doc.page_content
        print(f"URL: {url} - HTML Length: {len(html_content)}" if html_content else f"URL: {url} - Failed to fetch content.")

# Run the test
asyncio.run(test_scraper())
