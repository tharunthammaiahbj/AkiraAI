import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig

async def main():
    browser_config = BrowserConfig()  # Default browser configuration
    run_config = CrawlerRunConfig()   # Default crawl run configuration

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://docs.scrapy.org/en/latest/topics/downloader-middleware.html",
            config=run_config
        )
        
        # Save raw HTML to a file
        file_path = "/workspaces/AkiraAI/tests/sample_htmls/documentary3_html.html"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(result.html)  # Save raw HTML content
        print(f"HTML content saved to {file_path}")
        
        # Print some outputs for verification
        print(result.fit_markdown)  # Most relevant content in markdown

if __name__ == "__main__":
    asyncio.run(main())
