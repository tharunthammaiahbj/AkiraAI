import asyncio
from typing import AsyncIterator
from langchain_core.documents import Document
from playwright.async_api import async_playwright
from undetected_playwright import Malenia
from typing import Dict, Optional, List
from akiraai.utils.logging import get_logger
from akiraai.web_doc_loader.scraper_framework import ScraperFramework
from akiraai.utils.langchain_doc_converter import doc_converter
from akiraai.utils.clean_up_html import reduce_html


logger = get_logger("playwright-logger")


class PlaywrightAsyncScraper(ScraperFramework):

    def __init__(self, headless=True, retry_limit=3, proxy_mode="none", timeout=30, max_concurrency=3, **kwargs):

        super().__init__(headless, retry_limit, proxy_mode, timeout, **kwargs)
        self.max_concurrency = max_concurrency
        
            
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
            


    async def fetch_urls_with_browser(self, urls: List[str]) ->AsyncIterator[Document]:
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
                    if html_content:
                        cleaned_html = reduce_html(html=html_content, reduction=1)
                        doc = doc_converter(url=url, cleaned_html=cleaned_html)
                        yield doc

            except Exception as e:
                logger.error(f"Error during URL fetch process: {e}")

            finally:
                # Close all pages and browser
                for page in pages:
                    await page.close()
                await browser.close()



# <-------------------------------------------------------------------------------------->

"""
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
"""
                



        


  

        

           
