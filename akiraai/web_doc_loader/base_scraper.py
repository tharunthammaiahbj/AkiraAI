from abc import ABC , abstractmethod
from typing import List, Optional, Dict, Any
from utils.proxy_rotation import ProxyFilter, ProxyFetcher

class ScraperFramework(ABC):
    """
    Abstract Base Class for scraper frameworks.

    This class provides a standardized interface for all scraper implementations.
    """

    def __init__(
            self,
            headless : bool = True,
            retry_limit : int = 3,
            proxy_filter : Optional[ProxyFilter] = None,
            **kwargs : Any
                 ):
        
        """
        Initialize the base scraper.

        Args:
            headless (bool): Whether to run the scraper in headless mode.
            retry_limit (int): Number of retry attempts for failed requests.
            kwargs (Any): Additional configuration parameters.
        """

        self.headless = headless
        self.retry_limit = retry_limit
        self.proxies = ProxyFetcher(proxy_filter=proxy_filter) if proxy_filter else None
        self.config = kwargs
        

    @abstractmethod
    async def scrape_urls_async(self, urls: List[str]) -> Dict[str,str]:

        """
        Abstract method to scrape multiple URLs asynchronously.

        Args:
             urls (List[str]): A list of URLs to scrape.
        
        Returns:
            Dict[str, str]: A dictionary of URLs and their corresponding scraped content.

        """

        pass
         
                
       