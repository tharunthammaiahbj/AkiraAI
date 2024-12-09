from akiraai.web_doc_loader.undetected_chrome_driver import UndetectedChromeDriverScraper

scraper = UndetectedChromeDriverScraper(
    num_instances=3
)

urls = [
    "https://en.wikipedia.org/wiki/Deaths_in_2024",
    "https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers",
    "https://www.amazon.in/gp/bestsellers/automotive/ref=zg_bs_nav_automotive_0",
    "https://www.amazon.in/gp/bestsellers/automotive/5257482031/ref=zg_bs_nav_automotive_1",
    "https://www.amazon.in/gp/bestsellers/automotive/5257605031/ref=zg_bs_nav_automotive_2_5257482031"
]

results = scraper.process_urls_with_drivers(urls)

    # Print results
for url, html in results.items():
    if html:
        print(f"Success: {url} - Length: {len(html)}")
    else:
        print(f"Failed: {url}")

