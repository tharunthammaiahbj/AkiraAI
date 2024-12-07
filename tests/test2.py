import asyncio
import random
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options as ChromeOptions
from typing import List, Dict
from concurrent.futures import ThreadPoolExecutor
from aiohttp import ClientSession
from akiraai.utils.proxy_rotation import ProxyFetcher,ProxyFilter

class UndetectedChromeDriverScraper:
    def __init__(self, max_workers: int = 5, retry_limit: int = 3, proxy_mode: str = "none", headless: bool = True):
        self.max_workers = max_workers
        self.retry_limit = retry_limit
        self.proxy_mode = proxy_mode
        self.headless = headless
        self.semaphore = asyncio.Semaphore(max_workers)

    def _configure_proxies(self) -> str:
        """Configures and returns proxy settings if needed."""
        if self.proxy_mode == "freeproxy":
            # Assuming ProxyFetcher and ProxyFilter are properly defined elsewhere.
            proxy_filter = {
                "anonymous": True,
                "country_preference_set": None,
                "outside_search": True,
                "proxy_count": 5,
                "secure": False,
                "time_out": 5
            }
            proxy_fetcher = ProxyFetcher(proxy_filter=proxy_filter)
            proxy_list = proxy_fetcher.validated_proxy_list()
            return random.choice(proxy_list) if proxy_list else None
        elif self.proxy_mode == "scrapedo":
            return None
        return None

    def _configure_scraper(self) -> uc.Chrome:
        """Configure the Chrome driver with optional proxy settings."""
        options = ChromeOptions()
        options.headless = self.headless
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        proxy = self._configure_proxies()
        if proxy:
            options.add_argument(f"--proxy-server={proxy}")

        return uc.Chrome(options=options)

    async def scrape_url_async(self, url: str) -> str:
        """Fetches a single URL using undetected_chromedriver."""
        driver = None
        attempt = 0
        while attempt < self.retry_limit:
            try:
                driver = self._configure_scraper()
                driver.get(url)
                page_content = driver.page_source
                driver.quit()
                return page_content
            except Exception as e:
                attempt += 1
                if attempt == self.retry_limit:
                    return f"Error: Failed to fetch {url} after {self.retry_limit} attempts"
            finally:
                if driver:
                    driver.quit()

    async def scrape_urls_async(self, urls: List[str]) -> Dict[str, str]:
        """Concurrent URL scraping using undetected_chromedriver."""
        tasks = []
        for url in urls:
            tasks.append(self.scrape_url_with_pool(url))
        
        # Run all scraping tasks concurrently
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return {url: result for url, result in zip(urls, results)}

    async def scrape_url_with_pool(self, url: str) -> str:
        """Handles concurrency and browser pool management."""
        async with self.semaphore:
            return await self.scrape_url_async(url)

# Helper function for running the asynchronous code
async def main():
    scraper = UndetectedChromeDriverScraper(max_workers=5, retry_limit=3, proxy_mode="freeproxy", headless=True)

    urls = [
        "https://en.wikipedia.org/wiki/Deaths_in_2024",
        "https://www.amazon.in/iphone/s?k=iphone",
        "https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers",
        "https://www.amazon.in/gp/bestsellers/automotive/ref=zg_bs_nav_automotive_0",
        "https://www.amazon.in/gp/bestsellers/automotive/5257482031/ref=zg_bs_nav_automotive_1",
        "https://www.amazon.in/gp/bestsellers/automotive/5257605031/ref=zg_bs_nav_automotive_2_5257482031",
        "https://www.amazon.in/gp/bestsellers/automotive/5257606031/ref=zg_bs_nav_automotive_2_5257605031"
    ]
    
    results = await scraper.scrape_urls_async(urls)
    
    # Print results
    for url, content in results.items():
        print(f"URL: {url}\nContent Length: {len(content)}")

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
