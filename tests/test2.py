from akiraai.utils.proxy_rotation_new import ProxyFetcher,ProxyFilter


filter : ProxyFilter = {
    "allow_google":None,
    "anonymous":True,
    "country_preference":["US"],
    "secure":True,
    "outside_search_if_empty":True,
    "time_out":7,
    "max_proxies":6
}


proxyserver = ProxyFetcher(proxy_filter=filter)
print(f"ProxyList:{proxyserver.fetch_proxy_list()}")

