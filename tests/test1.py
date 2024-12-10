from typing import List, Dict, Optional
import asyncio
from playwright.async_api import async_playwright
from undetected_playwright import Malenia
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class URLFetcher:
    def __init__(self, max_concurrency: int = 3, headless: bool = True, timeout: int = 30):
        self.max_concurrency = max_concurrency
        self.headless = headless
        self.timeout = timeout

    async def fetch_url(self, page, url, semaphore, timeout: int = 30):
        """
        Fetches the HTML content of a URL using the given page.
        """
        async with semaphore:
            try:
                logger.info(f"Page is fetching URL: {url}")
                await page.goto(url, timeout=timeout * 1000)  # Timeout in milliseconds
                html_content = await page.content()
                logger.info(f"Page fetched URL: {url}")
                return html_content
            except Exception as e:
                logger.error(f"Error fetching {url}: {e}")
                return None

    async def fetch_urls_with_browser(self, urls: List[str]) -> Dict[str, Optional[str]]:
        """
        Fetches multiple URLs concurrently using a shared browser and pages.
        """
        results: Dict[str, Optional[str]] = {}
        semaphore = asyncio.Semaphore(self.max_concurrency)

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            await Malenia.apply_stealth(context=context)

            pages = [await context.new_page() for _ in range(self.max_concurrency)]

            try:
                # Assign tasks to pages
                tasks = []
                for i, url in enumerate(urls):
                    tasks.append(self.fetch_url(pages[i % self.max_concurrency], url, semaphore, self.timeout))

                # Gather results
                fetched_results = await asyncio.gather(*tasks)

                # Map results to URLs
                for url, html_content in zip(urls, fetched_results):
                    results[url] = html_content

            except Exception as e:
                logger.error(f"Error during URL fetch process: {e}")

            finally:
                # Close all pages and browser
                for page in pages:
                    await page.close()
                await browser.close()

        return results

# Test the URLFetcher class
if __name__ == "__main__":
    async def test_url_fetcher():
        urls = [
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

        fetcher = URLFetcher(max_concurrency=8, headless=True, timeout=30)
        results = await fetcher.fetch_urls_with_browser(urls)

        for url, html in results.items():
            if html:
                print(f"URL: {url}\nHTML Length: {len(html)}\n")
            else:
                print(f"URL: {url}\nFailed to fetch content.\n")

    # Run the test
    asyncio.run(test_url_fetcher())
