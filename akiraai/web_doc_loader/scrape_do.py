"""
Scrape_do module and API integration:
"""
import os
from dotenv import load_dotenv
import urllib.parse
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_do_fetch( target_url, geoCode=None, super_proxy=False, use_proxy =False):
    """
    Fetches the IP address of the machine associated with the given URL using Scrape.do.
    (i) "use_proxy" : 1 API Cost 
    (ii) "use_proxy" & "geoCode" : 1 API Cost
    (iii) "use_proxy" & "geoCode" & "super_proxy": 2 API Cost

    Args:
        
        target_url (str): A valid web page URL to fetch its associated IP address.
        geoCode (str, optional): Specify the country code for 
        geolocation-based proxies. Default is None.
        super_proxy (bool): If True, use Residential & Mobile Proxy Networks. Default is False.

    Returns:
        str: The raw response from the target URL.
    """
    load_dotenv()
    token = os.getenv("SCRAPE_DO_TOKEN")

    encoded_url = urllib.parse.quote(target_url)
    if use_proxy:
        proxy_mode_url = f"http://{token}:@proxy.scrape.do:8080"
        proxies = {
            "http": proxy_mode_url,
            "https": proxy_mode_url,
        }
        params = {"geoCode": geoCode, "super": str(super_proxy).lower()} if geoCode else {}
        response = requests.get(target_url, proxies=proxies, verify=False, params=params)
    else:
        url = f"http://api.scrape.do?token={token}&url={encoded_url}"
        response = requests.get(url)

    return response.text