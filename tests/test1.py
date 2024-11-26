from akiraai.web_doc_loader.chromium_loader import ChromiumLoader
import asyncio

async def scrape_single_page():
    url = "https://www.amazon.in/"

    scraper = ChromiumLoader(
        urls=[url] , headless=True, requires_js_support=True
    )
    content = await scraper.ascrape_with_js_support(url)

    print(content)

if __name__ == "__main__":
    asyncio.run(scrape_single_page())

