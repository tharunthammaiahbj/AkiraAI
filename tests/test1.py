proxy_mode =input("Enter the proxy_mode: ")

if proxy_mode:
    proxy_mode = proxy_mode.replace(" ","").lower()

if proxy_mode not in ['freeproxy', 'scrapedo', 'none']:
    raise ValueError(f"Invalid proxy_mode: {proxy_mode}. Valid options are 'freeproxy', 'scrapedo', or 'none'.")

print(proxy_mode)