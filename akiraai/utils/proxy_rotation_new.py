import ipaddress
import random
import re   
from typing import List, Optional, Set, TypedDict
import requests
from fp.errors import FreeProxyException
from fp.fp import FreeProxy

class ProxyFilter(TypedDict , total = False):

    anonymous:bool
    secure:bool
    time_out:float
    country_preference:Set[str]
    outside_search_if_empty:bool
    latency_limit: Optional[float]
    reliability_score: Optional[float]
    max_proxies: Optional[int]
    allow_google: Optional[bool]


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

    def fetch_proxy_list(self)->List[str]:
        try:
            candidates = self.proxybroker.get_proxy_list(
                self.proxy_filter.get("outside_search_if_empty", True)
            )
            return candidates
        except FreeProxyException as e:
            raise Exception(f"Failed to fetch proxies: {str(e)}")


