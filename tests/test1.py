from akiraai.web_doc_loader.undetected_chrome_driver import UndetectedChromeDriverScraper
import asyncio
import json

undetected_driver = UndetectedChromeDriverScraper(
    proxy_mode="none",
    max_workers=5
    )

def save_to_json(data, filename="scraped_results.json"):

    trimmed_data = {url: content[:500] if isinstance(content, str) else 'Error' for url, content in data.items()}
    
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(trimmed_data, json_file, ensure_ascii=False, indent=4)


urls = [
    "https://en.wikipedia.org/wiki/Deaths_in_2024",
    "https://www.amazon.in/iphone/s?k=iphone",
    "https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers",
    "https://www.amazon.in/gp/bestsellers/automotive/ref=zg_bs_nav_automotive_0",
    "https://www.amazon.in/gp/bestsellers/automotive/5257482031/ref=zg_bs_nav_automotive_1",
    "https://www.amazon.in/gp/bestsellers/automotive/5257605031/ref=zg_bs_nav_automotive_2_5257482031",
    "https://www.amazon.in/gp/bestsellers/automotive/5257606031/ref=zg_bs_nav_automotive_2_5257605031"

]

results = asyncio.run(undetected_driver.scrape_urls_async(urls=urls))

save_to_json(results)


for url, content in results.items():
        print(f"URL: {url}\nContent length: {len(content) if isinstance(content, str) else 'Error'}\n")




