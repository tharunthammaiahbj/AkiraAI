import asyncio
from crawl4ai.content_filter_strategy import PruningContentFilter
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai import AsyncWebCrawler, CacheMode, BrowserConfig, CrawlerRunConfig

async def clean_content():
    async with AsyncWebCrawler(verbose=True) as crawler:
        config = CrawlerRunConfig(
            cache_mode=CacheMode.ENABLED,
            excluded_tags=['nav', 'footer', 'aside'],
            remove_overlay_elements=True,
            markdown_generator=DefaultMarkdownGenerator(
                content_filter=PruningContentFilter(threshold=0.48, threshold_type="fixed", min_word_threshold=0),
                options={
                    "ignore_links": False
                }
            ),
        )
        result = await crawler.arun(
            url="https://www.ebay.com/sch/i.html?_nkw=Louis+Vuitton+Bags+%26+Handbags+for+Women+&_sacat=0&_from=R40&_trksid=p4439441.m570.l1313",
            config=config,
        )
        full_markdown_length = len(result.markdown_v2.raw_markdown)
        fit_markdown_length = len(result.markdown_v2.fit_markdown)
        print(f"Full Markdown Length: {full_markdown_length}")
        print(f"Fit Markdown Length: {fit_markdown_length}")
        
        # Save the fit markdown to a file
        with open("/workspaces/AkiraAI/clean_markdown.md", "w") as file:
            file.write(result.markdown_v2.fit_markdown)
        print("Fit markdown has been saved to /workspaces/AkiraAI/clean_markdown.md")

# Run the asynchronous function
asyncio.run(clean_content())
