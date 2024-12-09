from concurrent.futures import ThreadPoolExecutor
from undetected_chromedriver import Chrome, ChromeOptions
import os


def initialize_driver(profile_path):
    """
    Initializes a Chrome driver instance with a unique profile.
    """
    options = ChromeOptions()
    options.add_argument(f"user-data-dir={profile_path}")  # Assign unique profile
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")  # Optional for headless operation

    # Return the initialized Chrome driver
    return Chrome(options=options, user_multi_procs=True)


def fetch_url(driver, url):
    """
    Fetches the HTML content of a given URL using a driver.
    """
    try:
        driver.get(url)
        html = driver.page_source
        print(f"Fetched {len(html)} characters from {url}")
        return url, html
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return url, None


def process_urls_with_drivers(urls, profile_base_dir):
    """
    Processes a list of URLs using 3 Chrome drivers initialized with profiles.
    """
    # Ensure profile directories exist
    profiles = [os.path.join(profile_base_dir, f"profile_{i}") for i in range(3)]
    for profile in profiles:
        os.makedirs(profile, exist_ok=True)

    # Initialize 3 Chrome drivers
    drivers = [initialize_driver(profile) for profile in profiles]

    try:
        # Use ThreadPoolExecutor to manage concurrent URL fetching
        results = []
        with ThreadPoolExecutor(max_workers=3) as executor:
            # Assign URLs to drivers in a round-robin fashion
            futures = {
                executor.submit(fetch_url, drivers[i % 3], url): url for i, url in enumerate(urls)
            }
            for future in futures:
                results.append(future.result())

        return results
    finally:
        # Quit all drivers
        for driver in drivers:
            driver.quit()


if __name__ == "__main__":
    # List of URLs to process
    urls = [
         "https://en.wikipedia.org/wiki/Deaths_in_2024",
    "https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers",
    "https://www.amazon.in/gp/bestsellers/automotive/ref=zg_bs_nav_automotive_0",
    "https://www.amazon.in/gp/bestsellers/automotive/5257482031/ref=zg_bs_nav_automotive_1",
    "https://www.amazon.in/gp/bestsellers/automotive/5257605031/ref=zg_bs_nav_automotive_2_5257482031"
    ]

    # Base directory for storing Chrome profiles
    profile_base_dir = "./chrome_profiles"

    # Process URLs
    results = process_urls_with_drivers(urls, profile_base_dir)

    # Print results
    for url, html in results:
        if html:
            print(f"Success: {url} - Length: {len(html)}")
        else:
            print(f"Failed: {url}")
