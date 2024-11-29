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
        try:
            proxy_list = self.proxybroker.get_proxy_list(
                self.proxy_filter.get("outside_search", True)
            )
            abc = working_proxy_list(
                proxybroker=self.proxybroker,
                proxy_count=self.proxy_count,
                outside_search=self.proxy_filter.get("outside_search",True)
            )                        
        except FreeProxyException as e:
            raise Exception(f"Failed to fetch proxies: {str(e)}")
    
    



def working_proxy_list(proxybroker:FreeProxy, proxy_count: int, outside_search: bool):

        valid_proxies = set()

        proxy_list = proxybroker.get_proxy_list(outside_search)
        random.shuffle(proxy_list)

        for proxy in proxy_list:
            proxy_url = {proxybroker.schema: f"http://{proxy}"}

            try:
                proxy_server = proxybroker.__check_if_proxy_is_working(proxy_url)
                if proxy_server:
                    valid_proxies.add(proxy_server)
                if len(valid_proxies) >= proxy_count:
                    break
            except requests.exceptions.RequestException:
                continue

        if len(valid_proxies)<proxy_count:
            raise FreeProxyException("Not enough valid proxies found matching the criteria.")

        return list(valid_proxies)

        
        

