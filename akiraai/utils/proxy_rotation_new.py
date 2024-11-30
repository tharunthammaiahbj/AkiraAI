import ipaddress
import random
import re   
from typing import List, Optional, Set, TypedDict
import requests
from fp.errors import FreeProxyException
from fp.fp import FreeProxy
from akiraai.utils.logging import get_logger
import logging

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
    country_preference:Set[str]
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
         
    
    



def active_proxy_list(proxybroker:FreeProxy, proxy_count: int, outside_search: bool)->List[str]:
        

        valid_proxies = set()
        for _ in range(2):
            proxy_list = proxybroker.get_proxy_list(outside_search)
            random.shuffle(proxy_list)

            for element in proxy_list:
                 proxy_url = {proxybroker.schema: f"http://{element}"}

                 proxy_server =proxybroker._FreeProxy__check_if_proxy_is_working(proxy_url)

                 if proxy_server:
                      valid_proxies.add(proxy_server)

                 if len(valid_proxies) < proxy_count or not proxy_server:
                    continue
            
            n = len(valid_proxies)
            if len(valid_proxies)>=proxy_count:
                 break
            
            elif n<proxy_count and outside_search:
                 proxybroker.country_id=None

            else:
                 raise FreeProxyException("missing proxy servers for criteria")
        

        return list(valid_proxies)[:proxy_count]
            

        
        

