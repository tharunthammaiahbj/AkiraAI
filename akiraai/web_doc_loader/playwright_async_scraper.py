import asyncio
from playwright.async_api import async_playwright
from undetected_playwright import Malenia
from akiraai.web_doc_loader.scraper_framework import ScraperFramework
from typing import Dict,Optional,List


class PlaywrightAsyncScraper(ScraperFramework):
   
    """
    A concrete implementation of the ScraperFramework using Async Playwright.
    """

    def __init__(self, headless = True, retry_limit = 3, proxy_mode = "none", timeout = 30,max_concurrency = 3, **kwargs):
        

        super().__init__(headless, retry_limit, proxy_mode, timeout, **kwargs)
        self.max_concurrency = max_concurrency

    


    async def initialise_browser(self, headless: bool = True) -> Malenia:
        """
        Initializes a Playwright browser instance using Malenia for undetected browsing.

        Args:
            headless (bool): Whether to launch the browser in headless mode.
            max_concurrent_pages (int): Maximum number of concurrent pages.

        Returns:
            Malenia: An instance of Malenia for managing browser and pages.
        """
        # Initialize Playwright and use Malenia for undetected browsing
        playwright = await async_playwright().start()
        malenia = Malenia(playwright.chromium, headless=headless, max_concurrent_pages=self.max_concurrency)
    
        # Launch the browser with Malenia
        await malenia.start()
        return malenia
    

    async def fetch_url(self, malenia: Malenia, url: str, timeout: int = 30) -> Dict[str, Optional[str]]:
        """
        Fetches the HTML content of a single URL using Malenia-managed page.

        Args:
            malenia (Malenia): Malenia instance for undetected browsing.
            url (str): The URL to fetch.
            timeout (int): Timeout for the page load in seconds.

        Returns:
            dict: A dictionary with the URL as the key and the HTML content as the value.
        """
        try:
            # Open a new page with Malenia
            page = await malenia.new_page()

            # Navigate to the URL
            await page.goto(url, timeout=timeout * 1000)
            html = await page.content()

        # Return HTML content
            return {url: html}

        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return {url: None}
    
        finally:
            await page.close()

    

    async def process_urls_with_browsers(
        self,
        urls: List[str],
        headless: bool = True,
        timeout: int = 30,
        ) -> Dict[str, Optional[str]]:
        """
        Processes a list of URLs with concurrency using Malenia.

        Args:
            urls (List[str]): List of URLs to fetch.
            headless (bool): Whether to launch the browser in headless mode.
            timeout (int): Timeout for page loads in seconds.
            max_concurrency (int): Maximum number of concurrent pages/requests.

        Returns:
         dict: A dictionary mapping URLs to their HTML content.
        """

        max_concurrency = self.max_concurrency
        results: Dict[str, Optional[str]] = {}

        # Initialize Malenia browser instance
        malenia = await self.initialise_browser(headless=headless)
    
        try:
            # Create tasks to fetch URLs concurrently
            tasks = [self.fetch_url(malenia, url, timeout) for url in urls]
        
            # Gather results from all tasks concurrently
            results_list = await asyncio.gather(*tasks)

            # Combine results into a single dictionary
            for result in results_list:
                results.update(result)

        finally:
            # Stop Malenia browser instance once all tasks are completed
            await malenia.stop()

        return results



    