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
        self.proxy_mode = proxy_mode
        self.config = kwargs


    @abstractmethod
    def initialise_driver(self) -> Any:
        """
        Abstract method to configure the web driver or API client.

        Returns:
            Configured driver or client instance.
        """
        pass
