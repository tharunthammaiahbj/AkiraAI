from akiraai.web_doc_loader.playwright_async_scraper import PlaywrightAsyncScraper
import asyncio

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


# Initialize scraper
scraper = PlaywrightAsyncScraper(max_concurrency=3, timeout=30)

# Fetch URLs
results = asyncio.run(scraper.fetch_urls_with_browser(urls=url_list))

# Print the URL and the HTML content length
for url, html in results.items():
    if html is not None:
        print(f"URL: {url} - HTML Length: {len(html)}")
    else:
        print(f"URL: {url} - Failed to fetch content.")