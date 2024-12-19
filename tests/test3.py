import os
from akiraai.web_doc_loader.undetected_chrome_driver_async import UndetectedChromeDriverScraper

def main():
    scraper = UndetectedChromeDriverScraper(num_instances=3)

    urls = [
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

    # Get the results synchronously
    results = scraper.process_urls_with_drivers(urls)

    # Print the results
    for doc in scraper.process_urls_with_drivers(urls):
        if doc:  # If doc is not None
            print(f"Success: {doc.metadata['source']} - Length: {len(doc.page_content)}")
        else:
            print(f"Failed: {doc.metadata['source']}")

# Run the main function
if __name__ == "__main__":
    main()
