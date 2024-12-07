from akiraai.utils.proxy_rotation import ProxyFetcher, ProxyFilter
import random

proxy_filter : ProxyFilter = {} 
proxy_Fetcher = ProxyFetcher(proxy_filter=proxy_filter)
proxy_list = proxy_Fetcher.validated_proxy_list()
#random_proxy =random.choice(proxy_list)

print(f"Proxy List : {proxy_list}")
#print(f"Random Proxy: {random_proxy}")