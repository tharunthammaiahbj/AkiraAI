import asyncio
from akiraai.web_doc_loader.scraper_framework import ScraperFramework
from playwright.async_api import async_playwright
from undetected_playwright import Malenia
from typing import Dict, Optional, List
from akiraai.utils.logging import get_logger


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

                



        


  

        

           
