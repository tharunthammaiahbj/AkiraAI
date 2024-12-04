"""
Scrape.do API integration with TOKEN and using it.
scraping either using API directly or using the proxy servers.
"""
import asyncio
import aiohttp
import urllib.parse
from akiraai.utils.logging import get_logger

logger = get_logger(
    name="scrape.do-logger"
) 

async def fetch_single_url_scrape_do(session, token, target_url, js_render=False, geoCode=None, use_residential=False, use_proxy=False):
    """
    Fetches a URL using the Scrape.do API with provided options and optionally use proxy.

    Args:
        session (aiohttp.ClientSession): The aiohttp session for making requests.
        token (str): API token for Scrape.do.
        target_url (str): The URL to scrape.
        js_render (bool): Enable JavaScript rendering. Default is False.
        geoCode (str, optional): Country code for geotargeting. Default is None.
        use_residential (bool): Use residential or mobile proxies. Default is False.
        use_proxy (bool): Use Scrape.do proxy. Default is False.

    Returns:
        str: The response text or an error message.
    """
    encoded_url = urllib.parse.quote(target_url)
    url = f"http://api.scrape.do?token={token}&url={encoded_url}"

    # Add optional parameters
    params = {}
    if js_render:
        params["render"] = "true"
    if geoCode:
        params["geo"] = geoCode
    if use_residential:
        params["residential"] = "true"

    if use_proxy:
        # If using proxy, configure the proxy settings
        proxy_url = f"http://{token}:@proxy.scrape.do:8080"
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }
    else:
        proxies = {}

    try:
        async with session.get(url, params=params, proxy=proxies.get("http", None)) as response:
            if response.status == 200:
                return await response.text()
            else:
                logger.error(f"Failed to fetch {target_url}: {response.status}")
                return f"Error: {response.status} for {target_url}"
    except Exception as e:
        logger.error(f"Exception while fetching {target_url}: {e}")
        return f"Exception: {e}"


async def fetch_multiple_url_with_scrape_do(token, urls, js_render=False, geoCode=None, use_residential=False):
    """
    Fetches multiple URLs with concurrency control (5 concurrent requests max).

    Args:
        token (str): API token for Scrape.do.
        urls (list): List of URLs to scrape.
        js_render (bool): Enable JavaScript rendering for all requests. Default is False.
        geoCode (str, optional): Geotargeting country code. Default is None.
        use_residential (bool): Use residential or mobile proxies. Default is False.

    Returns:
        list: Responses from all URLs.
    """
    semaphore = asyncio.Semaphore(5)  # Limit to 5 concurrent requests
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(
                fetch_with_semaphore(
                    semaphore, session, token, url, js_render, geoCode, use_residential
                )
            )
            for url in urls
        ]
        results = await asyncio.gather(*tasks)
    return results

async def fetch_with_semaphore(semaphore, session, token, target_url, js_render, geoCode, use_residential):
    """
    Wrapper to apply semaphore to fetch_with_scrape_do.

    Args:
        semaphore (asyncio.Semaphore): Semaphore to control concurrency.
        session (aiohttp.ClientSession): The aiohttp session for making requests.
        token (str): API token for Scrape.do.
        target_url (str): The URL to scrape.
        js_render (bool): Enable JavaScript rendering. Default is False.
        geoCode (str, optional): Country code for geotargeting. Default is None.
        use_residential (bool): Use residential or mobile proxies. Default is False.

    Returns:
        str: The response from the URL fetch.
    """
    async with semaphore:
        return await fetch_single_url_scrape_do(session, token, target_url, js_render, geoCode, use_residential)
