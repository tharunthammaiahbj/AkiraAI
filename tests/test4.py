import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig

async def main():
    browser_config = BrowserConfig()  # Default browser configuration
    run_config = CrawlerRunConfig()   # Default crawl run configuration

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://www.amazon.in/gp/bestsellers/luggage/ref=zg_bs_nav_luggage_0",
            config=run_config
        )
        
        # Save raw HTML to a file
        '''file_path = "/workspaces/AkiraAI/tests/sample_htmls/documentary3_html.html"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(result.html)  # Save raw HTML content
        print(f"HTML content saved to {file_path}")'''

        with open("/workspaces/AkiraAI/tests/sample_markdowns/cleaned_amazon1_md.md", "w", encoding="utf-8") as file:
            file.write(result.markdown)  # Save raw HTML content
        #print(f"HTML content saved to {file_path}")
        
        # Print some outputs for verification
        print(result.markdown)  # Most relevant content in markdown

if __name__ == "__main__":
    asyncio.run(main())
