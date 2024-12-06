from akiraai.web_doc_loader.undetected_chrome_driver import UndetectedChromeDriverScraper  # Replace with the actual module and class name
from akiraai.utils.logging import get_logger

# Set up logging for visibility
logger = get_logger(name="test-logger")

def test_configure_driver():
    """
    Test the `_configure_driver` function to ensure it configures and initializes a Chrome driver correctly.
    """
    try:
        # Initialize your class with required parameters
        instance = UndetectedChromeDriverScraper(headless=True)  # Add additional arguments if necessary

        # Call the `_configure_driver` method
        driver = instance._configure_driver()

        # Test driver functionality by loading a test URL
        test_url = "https://en.wikipedia.org/wiki/Geopolitics"
        logger.info(f"Opening test URL: {test_url}")
        driver.get(test_url)

        # Get the entire HTML content of the page
        page_html = driver.page_source
        logger.info(f"HTML content retrieved. Length of HTML: {len(page_html)} characters")

        # You can also log the first 500 characters of the page content (if needed)
        logger.debug(f"First 500 characters of the page: {page_html[:500]}")

        # Quit the driver after test
        driver.quit()
        logger.info("Driver successfully configured and tested!")
    except Exception as e:
        logger.error(f"Error during testing: {e}")

if __name__ == "__main__":
    test_configure_driver()
