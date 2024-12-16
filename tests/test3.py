from akiraai.web_doc_loader.undetected_chrome_driver import UndetectedChromeDriverScraper

# Define test URLs
url_list = [
    "https://en.wikipedia.org/wiki/Deaths_in_2024",
    "https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers",
    "https://www.amazon.in/gp/bestsellers/automotive/ref=zg_bs_nav_automotive_0",
    "https://www.amazon.in/gp/bestsellers/automotive/5257482031/ref=zg_bs_nav_automotive_1",
    "https://www.amazon.in/gp/bestsellers/automotive/5257605031/ref=zg_bs_nav_automotive_2_5257482031",
    "https://www.amazon.in/gp/bestsellers/automotive/5257477031/ref=zg_bs_nav_automotive_1",
    "https://www.amazon.in/gp/bestsellers/automotive/5257556031/ref=zg_bs_nav_automotive_2_5257477031",
    "https://www.amazon.in/gp/bestsellers/automotive/51396100031/ref=zg_bs_nav_automotive_2_5257556031",
    "https://www.amazon.in/gp/bestsellers/gift-cards/92070982031/ref=zg_bs_nav_gift-cards_1",
    "https://www.amazon.in/gp/bestsellers/gift-cards/92070985031/ref=zg_bs_nav_gift-cards_1_92070982031"
]

# Initialize the scraper
scraper = UndetectedChromeDriverScraper(num_instances=3)

# Define a function to fetch URLs and print the results
def test_scraper():
    # Call the method that scrapes the URLs
    for doc in scraper.process_urls_with_drivers(urls=url_list):
        # For each document, print the URL, title, and content length
        print(f"Document URL: {doc.metadata['source']}")
        print(f"Title: {doc.metadata['title']}")
        print(f"Content Length: {len(doc.page_content)}")
        print('-' * 50)

# Run the test
test_scraper()
