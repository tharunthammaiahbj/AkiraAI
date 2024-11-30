import ipaddress
import random
import re   
from typing import List, Optional, Set, TypedDict
import requests
from fp.errors import FreeProxyException
from fp.fp import FreeProxy

class ProxyBrokerCriteria(TypedDict, total=False):
    """
    Proxy broker criteria for rotating proxies:
    The ProxyBrokerCriteria class is used to define a flexible and customizable 
    set of conditions for selecting proxies, especially in the context of proxy 
    rotation for tasks like web scraping.
    
    """
    anonymous: bool  # Ensure the proxy is anonymous to prevent detection.
    countryset: Set[str]  # Allow country-specific proxies.
    secure: bool  # Whether proxies should support HTTPS.
    timeout: float  # Set the maximum timeout for proxies.
    search_outside_if_empty: bool  # Allow broader search if no proxies match.

class ProxySettings(TypedDict, total=False):
    """
    Configuration for each proxy, including authentication details.
    """
    server: str  # The proxy server address.
    bypass: str  # Addresses that should bypass the proxy (e.g., APIs).
    username: str  # Username for proxy authentication.
    password: str  # Password for proxy authentication.

class Proxy(ProxySettings):
    """
    Proxy server information including additional criteria.
    """
    criteria: ProxyBrokerCriteria  # Proxy criteria for filtering.

def search_proxy_servers(
    anonymous: bool = True,
    countryset: Optional[Set[str]] = None,
    secure: bool = False,
    timeout: float = 5.0,
    max_shape: int = 6,
    search_outside_if_empty: bool = True,
) -> List[str]:
    """Search for proxy servers that match specified criteria."""
    proxybroker = FreeProxy(
        anonym=anonymous,
        country_id=countryset,
        elite=True,
        https=secure,
        timeout=timeout,
    )

    def search_all(proxybroker: FreeProxy, k: int, search_outside: bool) -> List[str]:
        candidateset = proxybroker.get_proxy_list(search_outside)
        random.shuffle(candidateset)
        positive = set()

        for address in candidateset:
            setting = {proxybroker.schema: f"http://{address}"}

            try:
                server = proxybroker._FreeProxy__check_if_proxy_is_working(setting)

                if not server:
                    continue

                positive.add(server)

                if len(positive) < k:
                    continue

                return list(positive)

            except requests.exceptions.RequestException:
                continue

        n = len(positive)
        if n < k and search_outside:
            proxybroker.country_id = None
            try:
                negative = set(search_all(proxybroker, k - n, False))
            except FreeProxyException:
                negative = set()
            positive = positive | negative

        if not positive:
            raise FreeProxyException("missing proxy servers for criteria")

        return list(positive)

    return search_all(proxybroker, max_shape, search_outside_if_empty)  

def _parse_proxy(proxy: ProxySettings) -> ProxySettings:
    """Parses a proxy configuration."""
    assert "server" in proxy, "missing server in the proxy configuration"
    authorization = [x in proxy for x in ("username", "password")]
    assert all(authorization) or not any(authorization), "username and password must be provided in pairs or not at all"
    parsed = {"server": proxy["server"]}

    if proxy.get("bypass"):
        parsed["bypass"] = proxy["bypass"]

    if all(authorization):
        parsed["username"] = proxy["username"]
        parsed["password"] = proxy["password"]

    return parsed

def _search_proxy(proxy: Proxy) -> ProxySettings:
    """Searches for a proxy server matching the specified criteria."""
    criteria = proxy.get("criteria", {}).copy()
    criteria.pop("max_shape", None)
    server = search_proxy_servers(max_shape=1, **criteria)[0]
    return {"server": server}

def is_ipv4_address(address: str) -> bool:
    """Checks if the proxy address is a valid IPv4 address."""
    try:
        ipaddress.IPv4Address(address)
        return True
    except ipaddress.AddressValueError:
        return False

def parse_or_search_proxy(proxy: Proxy) -> ProxySettings:
    """Parses or searches for a proxy server."""
    assert "server" in proxy, "missing server in the proxy configuration"
    server_address = re.sub(r'^\w+://', '', proxy["server"]).split(":", maxsplit=1)[0]

    if is_ipv4_address(server_address):
        return _parse_proxy(proxy)

    assert proxy["server"] == "broker", "unknown proxy server"
    return _search_proxy(proxy)
