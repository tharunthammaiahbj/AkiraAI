import ipaddress
import random
import re   
from typing import List, Optional, Set, TypedDict
import requests
from fp.errors import FreeProxyException
from fp.fp import FreeProxy
from akiraai.utils.logging import get_logger
import logging
from concurrent.futures import ThreadPoolExecutor,as_completed

logger = get_logger("proxy-logger")

# Configure the named logger
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()  # Add a handler explicitly
handler.setFormatter(logging.Formatter(
    fmt=
    (
        "%(asctime)s [%(levelname)s] [%(name)s] "
        "[%(filename)s:%(lineno)d] - %(message)s"
    ),
    datefmt="%Y-%m-%d %H:%M:%S"))
logger.addHandler(handler)

class ProxyFilter(TypedDict , total = False):

    anonymous:bool
    secure:bool
    time_out:float
    country_preference_set:Set[str]
    outside_search:bool
    proxy_count: Optional[int]


class ProxyAuth(TypedDict, total=False):

    server: str  
    bypass: str  
    username: str 
    password: str 

class ProxyFetcher:
    def __init__(self, proxy_filter:ProxyFilter):

        self.proxy_filter = proxy_filter
        
        self.proxybroker = FreeProxy(
            anonym=self.proxy_filter.get("anonymous",True),
            https=self.proxy_filter.get("secure",False),
            country_id=self.proxy_filter.get("country_preference",None),
            timeout=self.proxy_filter.get("time_out",5.0),
            elite=True,            
        )
        self.proxy_count =self.proxy_filter.get("proxy_count",5)

    def validated_proxy_list(self)->List[str]:
         return active_proxy_list(
              proxybroker=self.proxybroker,
              proxy_count=self.proxy_count,
              outside_search=self.proxy_filter.get("outside_search",True),
         )
         
    
    



def active_proxy_list(proxybroker, proxy_count: int, outside_search: bool) -> List[str]:
    """
    Fetch a list of active proxies that satisfy the given criteria.

    Args:
        proxybroker (FreeProxy): The proxy broker object.
        proxy_count (int): The number of proxies required.
        outside_search (bool): Whether to search outside the initial criteria.

    Returns:
        List[str]: A list of validated proxy URLs.

    Raises:
        FreeProxyException: If the required number of proxies cannot be found.
    """
    valid_proxies: Set[str] = set()
    max_threads = 10  # Limit concurrent threads to avoid excessive resource use

    def validate_proxy(proxy_url: dict) -> str:
        """Validate a single proxy and return it if working."""
        try:
            return proxybroker._FreeProxy__check_if_proxy_is_working(proxy_url)
        except requests.exceptions.RequestException:
            return None

    while len(valid_proxies) < proxy_count:
        # Get a new batch of candidate proxies
        proxy_list = proxybroker.get_proxy_list(outside_search)
        random.shuffle(proxy_list)

        # Concurrently validate proxies
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            future_to_proxy = {
                executor.submit(validate_proxy, {proxybroker.schema: f"http://{proxy}"}): proxy
                for proxy in proxy_list
            }

            for future in as_completed(future_to_proxy):
                try:
                    result = future.result()
                    if result:
                        valid_proxies.add(result)

                    # Early termination if required proxies are validated
                    if len(valid_proxies) >= proxy_count:
                        return list(valid_proxies)[:proxy_count]
                except Exception:
                    continue  # Ignore any exceptions

        # Broaden search criteria if insufficient proxies are found
        if len(valid_proxies) < proxy_count and outside_search:
            proxybroker.country_id = None  # Remove country restrictions

    # Raise an exception if not enough proxies are found
    if len(valid_proxies) < proxy_count:
        raise FreeProxyException(f"Only found {len(valid_proxies)} proxies, but {proxy_count} required.")

    return list(valid_proxies)[:proxy_count]

            


        
        

