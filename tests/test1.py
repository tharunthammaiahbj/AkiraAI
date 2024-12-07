from akiraai.utils.proxy_rotation import ProxyFetcher,ProxyFilter
import random




proxy_filter : ProxyFilter = {
                 "anonymous":True,
                 "country_preference_set":None,
                 "outside_search":True,
                 "proxy_count": 5,
                 "secure":False,
                 "time_out":5
             }
proxy_fetcher = ProxyFetcher(proxy_filter=proxy_filter)
proxy_list = proxy_fetcher.validated_proxy_list()
print(proxy_list)
random_proxy = random.choice(proxy_list)
print(random_proxy)
 
