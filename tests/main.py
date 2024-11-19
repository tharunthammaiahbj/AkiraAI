import asyncio
from playwright.async_api import async_playwright
from undetected_playwright import Malenia

async def test_imports():
    """
    Test if Playwright and undetected-playwright are working correctly by scraping a page title.
    """
    try:
        print("Testing Playwright and undetected-playwright imports...")

        # Use Playwright with stealth modifications
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()

            # Apply stealth techniques
            await Malenia.apply_stealth(context)

            page = await context.new_page()
            await page.goto("https://playwright.dev/docs/writing-tests", wait_until="domcontentloaded")

            # Print the page title to verify everything is working
            title = await page.title()
            print(f"Page Title: {title}")

            # Close browser
            await browser.close()

        print("Imports and basic functionality work fine!")
    except Exception as e:
        print(f"Error: {e}")

# Run the test
asyncio.run(test_imports())
