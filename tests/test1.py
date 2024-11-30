from akiraai.utils.proxy_rotation import search_proxy_servers

proxy = search_proxy_servers(
    anonymous=True,
    countryset=["US"],
    secure=False,
       
)

print(proxy)
