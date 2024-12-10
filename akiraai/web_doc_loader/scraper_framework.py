import random
from abc import ABC, abstractmethod
from typing import Optional, Any
from akiraai.utils.logging import get_logger
from akiraai.utils.proxy_rotation import ProxyFetcher,ProxyFilter




logger = get_logger("scraper-framework-logger")


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
    

    def _configure_proxies(self) -> Optional[str]:
        """
        Configures proxy management based on the selected proxy_mode.
        """
        if self.proxy_mode == "freeproxy":
            logger.info("Freeproxy mode selected. Configuring a random free proxy.")
            proxy_filter : ProxyFilter = {
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


    @abstractmethod
    def initialise_driver(self) -> Any:
        """
        Abstract method to configure the web driver or API client.

        Returns:
            Configured driver or client instance.
        """
        pass
