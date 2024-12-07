from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from akiraai.utils.proxy_rotation import ProxyFilter, ProxyFetcher
from concurrent.futures import ThreadPoolExecutor

class ScraperFramework(ABC):
    """
    Abstract Base Class for scraper frameworks.

    This class provides a standardized interface for all scraper implementations.
    """

    def __init__(
            self,
            headless: bool = True,
            retry_limit: int = 3,
            proxy_mode : Optional[str] = "none",
            timeout: int = 30,
            max_workers: int = 10,  # Max concurrent threads
            **kwargs: Any
    ):
        """
        Initialize the base scraper.

        Args:
            headless (bool): Whether to run the scraper in headless mode.
            retry_limit (int): Number of retry attempts for failed requests.
            timeout (int): Timeout for requests or page loads (in seconds).
            max_workers (int): Maximum number of concurrent threads for fetching URLs.
            kwargs (Any): Additional configuration parameters.
        """

        if proxy_mode:
            proxy_mode = proxy_mode.replace(" ", "").lower()
            if proxy_mode not in ['freeproxy', 'scrapedo', 'none']:
                 raise ValueError(f"Invalid proxy_mode: {proxy_mode}. Valid options are 'freeproxy', 'scrapedo', or 'none'.")
       

        self.headless = headless
        self.retry_limit = retry_limit
        self.timeout = timeout
        self.max_workers = max_workers
        self.proxy_mode = proxy_mode
        self.config = kwargs
        self.executor = ThreadPoolExecutor(max_workers=self.max_workers)


    @abstractmethod
    def _configure_scraper(self) -> Any:
        """
        Abstract method to configure the web driver or API client.

        Returns:
            Configured driver or client instance.
        """
        pass

    async def _fetch_url_async(self, url: str) -> str:
        """
        Asynchronous wrapper to fetch a single URL (could be through a headless browser or API).

        Args:
            url (str): URL to fetch.

        Returns:
            str: The scraped content (HTML or JSON) of the URL.
        """
        # This function can be overridden in concrete implementations for async URL fetching
        raise NotImplementedError("This method must be implemented in the subclass")


    @abstractmethod
    async def scrape_urls_async(self, urls: List[str]) -> Dict[str, str]:
        """
        Abstract method to scrape multiple URLs asynchronously.

        Args:
            urls (List[str]): A list of URLs to scrape.

        Returns:
            Dict[str, str]: A dictionary of URLs and their corresponding scraped content.
        """
        pass