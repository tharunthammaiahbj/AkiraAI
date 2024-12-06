import asyncio
from akiraai.web_doc_loader.undetected_chrome_driver import UndetectedChromeDriverScraper  # Replace with actual module and class name
from akiraai.utils.logging import get_logger

# Set up logging for visibility
logger = get_logger(name="test-logger")

async def test_scrape_url_async():
    """
    Test the `scrape_url_async` function to ensure it fetches HTML content correctly.
    """
    try:
        # Initialize the scraper instance
        scraper = UndetectedChromeDriverScraper(headless=True, retry_limit=3)  # Adjust parameters as needed

        # URL to test
        test_url = "https://en.wikipedia.org/wiki/Geopolitics"

        logger.info(f"Testing URL: {test_url}")
        html_content = await scraper.scrape_url_async(test_url)

        # Verify if content was fetched
        if "Geopolitics" in html_content:
            logger.info("HTML content fetched successfully!")
        else:
            logger.warning("Failed to fetch the expected content.")

        # Optionally, print the first 500 characters of the content
        print(html_content[:500])
    except Exception as e:
        logger.error(f"Error during test: {e}")

if __name__ == "__main__":
    asyncio.run(test_scrape_url_async())
