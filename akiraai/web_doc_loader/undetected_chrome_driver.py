import random
import os
from typing import Optional, List, Dict
from concurrent.futures import ThreadPoolExecutor, as_completed
from akiraai.web_doc_loader.scraper_framework import ScraperFramework
from undetected_chromedriver import Chrome, ChromeOptions
from akiraai.utils.logging import get_logger
from akiraai.utils.proxy_rotation import ProxyFetcher, ProxyFilter

logger = get_logger(name="undetected_chrome_driver_logger")

class UndetectedChromeDriverScraper(ScraperFramework):
    """
    A concrete implementation of the ScraperFramework using undetected_chromedriver.
    """

    def __init__(self, num_instances: int, headless: bool = True, retry_limit: int = 3, 
             proxy_mode: str = "none", timeout: int = 30, **kwargs):
        """
        Initialize the scraper with instance count and other configuration.

        Args:
            num_instances (int): Number of Chrome driver instances to initialize.
            headless (bool): Whether to run the scraper in headless mode (default True).
            retry_limit (int): Number of retry attempts for failed requests (default 3).
            proxy_mode (str): Mode of proxy configuration (default "none").
            timeout (int): Timeout for requests or page loads (default 30).
            kwargs: Additional arguments passed to the parent class constructor.
        """
        # Pass the parent class parameters explicitly
        super().__init__(headless=headless, retry_limit=retry_limit, proxy_mode=proxy_mode,
                     timeout=timeout, **kwargs)
    
        # Initialize the child-specific parameters
        self.num_instances = num_instances



    def _configure_proxies(self) -> Optional[str]:
        """
        Configures proxy management based on the selected proxy_mode.
        """
        if self.proxy_mode == "freeproxy":
            logger.info("Freeproxy mode selected. Configuring a random free proxy.")
            proxy_filter = {
                "anonymous": True,
                "country_preference_set": None,
                "outside_search": True,
                "proxy_count": 5,
                "secure": False,
                "time_out": 5,
            }
            proxy_fetcher = ProxyFetcher(proxy_filter=proxy_filter)
            proxy_list = proxy_fetcher.validated_proxy_list()
            if proxy_list:
                random_proxy = random.choice(proxy_list)
                return random_proxy
            else:
                logger.warning("No valid proxies found. Proceeding without proxy.")
        elif self.proxy_mode == "scrapedo":
            logger.info("Scrape.do proxy mode selected. Will use scrape_do_fetch for requests.")
        elif self.proxy_mode == "none":
            logger.info("Proceeding without Proxy Configuration...")
        return None

    def initialise_driver(self, profile_path: str) -> Chrome:
        """
        Configures and returns an instance of the Chrome driver with optional proxy settings.
        """
        options = ChromeOptions()
        options.headless = self.headless
        options.add_argument(f"user-data-dir={profile_path}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Proxy management:
        proxy = self._configure_proxies()
        if self.proxy_mode == "freeproxy" and proxy:
            options.add_argument(f"--proxy-server={proxy}")
            logger.info(f"Proxy configured: {proxy}")

        try:
            return Chrome(options=options, user_multi_procs=True)
        except Exception as e:
            logger.error(f"Failed to Configure the Chrome Driver: {e}")
            raise

    def fetch_url(self, driver: Chrome, url: str) -> Dict[str, Optional[str]]:
        """
        Fetches the HTML content of a given URL using a driver.
        """
        try:
            driver.get(url)
            html = driver.page_source
            logger.info(f"Fetched {len(html)} characters from {url}")
            return url, html
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return url, None

    def process_urls_with_drivers(self, urls: List[str]) -> Dict[str, Optional[str]]:
        """
        Processes a list of URLs using multiple Chrome drivers initialized with profiles.
        Returns a dictionary mapping URLs to their HTML content.
        """

        profile_base_dir = "./chrome_profiles"
        profiles = [os.path.join(profile_base_dir, f"profile_{i}") for i in range(self.num_instances)]
        drivers = []
        results: Dict[str, Optional[str]] = {}

        try:
            # Initialize drivers
            for profile in profiles:
                os.makedirs(profile, exist_ok=True)
                drivers.append(self.initialise_driver(profile))

            # Fetch URLs concurrently
            with ThreadPoolExecutor(max_workers=self.num_instances) as executor:
                futures = {
                    executor.submit(self.fetch_url, drivers[i % self.num_instances], url): url
                    for i, url in enumerate(urls)
                }
                for future in as_completed(futures):
                    url, html = future.result()
                    results[url] = html  # Store the HTML content keyed by URL

            return results

        except Exception as e:
            logger.error(f"Error during URL processing: {e}")
            raise
        finally:
            # Close all drivers
            for driver in drivers:
                try:
                    driver.quit()
                except Exception as e:
                    logger.warning(f"Failed to close driver: {e}")
