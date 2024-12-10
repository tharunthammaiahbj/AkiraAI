import asyncio
from akiraai.web_doc_loader.scraper_framework import ScraperFramework
from playwright.async_api import async_playwright
from undetected_playwright import Malenia
from typing import Dict, Optional, List
from akiraai.utils.logging import get_logger


logger = get_logger("playwright-logger")


class PlaywrightAsyncScraper(ScraperFramework):

    def __init__(self, headless=True, retry_limit=3, proxy_mode="none", timeout=30, max_concurrency=3, **kwargs):
        """
        Initializes the PlaywrightAsyncScraper with necessary configurations.
        """
        super().__init__(headless, retry_limit, proxy_mode, timeout, **kwargs)
        self.max_concurrency = max_concurrency
        logger.info(f"Initialized PlaywrightAsyncScraper with max_concurrency={self.max_concurrency}, headless={headless}, retry_limit={retry_limit}, proxy_mode={proxy_mode}, timeout={timeout}")

    async def initialise_browser(self):
        """
        Initializes a Playwright browser instance and returns the browser and context.

        Args:
            headless (bool): Whether to launch the browser in headless mode.

        Returns:
            browser: An initialized Playwright browser instance.
            context: A new browser context for managing pages.
        """
        logger.info("Initializing browser and context...")
        proxy = self._configure_proxies()
        async with async_playwright() as p:
            logger.info("Launching Chromium browser...")
            browser = await p.chromium.launch(headless=self.headless, proxy=proxy)
            logger.info("Browser launched successfully.")

            logger.info("Creating new browser context...")
            context = await browser.new_context()
            logger.info("Browser context created successfully.")
            return browser, context

    async def fetch_urls_with_browser(self, urls: List[str], timeout: int = 30) -> Dict[str, Optional[str]]:
        """
        Processes a list of URLs with concurrency using Playwright and Malenia for undetected browsing.

        Args:
            urls (List[str]): List of URLs to fetch.
            timeout (int): Timeout for page loads in seconds.

        Returns:
            dict: A dictionary mapping URLs to their HTML content.
        """
        results: Dict[str, Optional[str]] = {}

        logger.info(f"Starting to fetch {len(urls)} URLs with max_concurrency={self.max_concurrency} and timeout={timeout} seconds.")

        # Initialize Playwright and browser context
        pages = []  # Initialize pages here to prevent UnboundLocalError
        try:
            self.browser, self.context = await self.initialise_browser()

            # Apply Malenia stealth to the context before creating pages
            logger.info("Applying Malenia stealth mode...")
            await Malenia.apply_stealth(self.context)
            logger.info("Malenia stealth applied successfully.")

            # Create pages based on concurrency limit
            logger.info(f"Creating {self.max_concurrency} pages based on concurrency limit...")
            pages = [await self.context.new_page() for _ in range(self.max_concurrency)]
            logger.info(f"{len(pages)} pages created.")

            # Create tasks to fetch URLs using the pages
            semaphore = asyncio.Semaphore(self.max_concurrency)

            async def fetch_with_semaphore(page, url):
                async with semaphore:
                    try:
                        logger.info(f"Fetching URL: {url} with page {page}")
                        result = await self.fetch_url(page, url, timeout)
                        logger.info(f"Successfully fetched {url}")
                        return {url: result}
                    except Exception as e:
                        logger.error(f"Error fetching {url}: {e}")
                        return {url: None}

            # Assign URLs to pages and fetch concurrently
            tasks = [fetch_with_semaphore(pages[i % self.max_concurrency], url) for i, url in enumerate(urls)]

            # Gather results from all tasks concurrently
            logger.info(f"Gathering results from {len(tasks)} fetch tasks concurrently...")
            results_list = await asyncio.gather(*tasks)

            # Combine results into a single dictionary
            for result in results_list:
                results.update(result)

        except Exception as e:
            logger.error(f"An error occurred during the fetch operation: {e}")
        finally:
            # Close all pages and the browser, checking that pages are initialized
            if pages:
                logger.info("Closing pages and browser...")
                for page in pages:
                    await page.close()
            if self.browser:
                await self.browser.close()
            logger.info("Browser and pages closed successfully.")

        logger.info(f"Completed fetching URLs. Returning {len(results)} results.")
        return results
