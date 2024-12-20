"""
AFTER REBUILDING CONTAINER----------------------------------------------------------------
This Module is mainly for correcting the undetected Chromedriver for proper execution :
return Chrome(options=options, user_multi_procs=True)
set it to False :
Run this script : Will get Errors 
Set it to True :
Should Work like Expected
"""
from akiraai.web_doc_loader.undetected_chrome_driver_async_scraper import UndetectedChromeDriverScraper

scraper = UndetectedChromeDriverScraper(
    num_instances=3
)

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

# Get the generator from the scraper
results = scraper.process_urls_with_drivers(urls)

# Process results
for doc in results:
    if doc:  # If doc is not None
        print(f"Success: {doc.metadata['source']} - Length: {len(doc.page_content)}")
    else:
        print(f"Failed: {doc.metadata['source']}")
