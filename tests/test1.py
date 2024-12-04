import asyncio
import aiohttp
from akiraai.web_doc_loader.scrape_do import fetch_single_url_scrape_do  # Replace with the actual file name

async def test_fetch_single_url():
    TOKEN = "930002fa47f249da87613f0555eefad972d6bc934aa"  # Replace with your Scrape.do API token
    TARGET_URL = "https://sale.alibaba.com/p/rank/list.html?spm=a2700.product_home_newuser.scenario_overview.topRanking&wx_navbar_transparent=true"  # Replace with a test URL

    async with aiohttp.ClientSession() as session:
        response = await fetch_single_url_scrape_do(
            session,
            token=TOKEN,
            target_url=TARGET_URL,
            js_render=False,  # Set to True if the target URL requires JavaScript rendering
            geoCode="US",  # Optional: Set to a specific country if needed
            use_residential=False  # Optional: Use residential proxies if required
        )
        print(response)

# Run the test function
if __name__ == "__main__":
    asyncio.run(test_fetch_single_url())
