try:
    # Attempt to import the Proxy class from akiraai.utils
    from akiraai.utils import Proxy, search_proxy_servers

    # Check if the Proxy class is accessible
    proxy_instance = Proxy()
    print("Proxy Instance Created:", proxy_instance)

    # Check if the function is accessible and works
    print("Testing search_proxy_servers:", search_proxy_servers())
    
    print("Import Test Passed! All components are working.")
except ImportError as e:
    print(f"Import Error: {e}")
except Exception as e:
    print(f"Error occurred: {e}")
