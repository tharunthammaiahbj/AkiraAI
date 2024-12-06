from langchain_community.document_loaders.base import BaseLoader
from akiraai.utils.logging import get_logger
from typing import Any, List, Optional, Iterator, AsyncIterator
from utils.proxy_rotation import ProxyFilter,ProxyFetcher

logger = get_logger(
    name="scrape-infra-logger"
)


class WebContentLoader(BaseLoader):
    """
    It scraping the HTML from the list of URLs using either "playwright" or "undetected chromedriver"
    """

    def __init__(
        self,
        urls:List[str],
        scraper_engine: str = "playwright",
        headless: bool = True,
        proxy_filter : Optional[ProxyFilter] = None,
    ):
        """
        Initializes and launches the scraper engine with a provided list of URLs for processing and content extraction.

        Args:
            urls (List[str]): A list of URLs to scrape content from.
            scraper_engine (str, optional): The scraper engine to use (default is "playwright").
            headless (bool, optional): Whether to run the browser in headless mode (default is True).
            proxy_filter (Optional[ProxyFilter], optional): A filter for proxy settings (default is None).
            **kwargs (Any): Additional keyword arguments for scraper configuration.
        """

        self.scraper_engine = scraper_engine
        self.urls = urls
        self.headless = headless
        self.proxies = ProxyFetcher(proxy_filter=proxy_filter) if proxy_filter else None
        


    
    
         
       


