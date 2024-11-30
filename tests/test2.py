from akiraai.utils.proxy_rotation_new import ProxyFetcher,ProxyFilter,active_proxy_list



filter : ProxyFilter = {
    "anonymous":True,
    "country_preference":["US"],
    "secure":False,
    "outside_search":True,
    "time_out":5,
    "proxy_count":6
}


proxyserver = ProxyFetcher(proxy_filter=filter)
print(f"ProxyList:{proxyserver.validated_proxy_list()}")



