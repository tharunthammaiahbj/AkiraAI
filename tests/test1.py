import asyncio
from playwright.async_api import async_playwright
from undetected_playwright import Malenia


async def main():

    url = "https://www.amazon.in/gp/bestsellers/?ref_=nav_cs_bestsellers"
    output_file = "output.html"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        await Malenia.apply_stealth(context=context)
        page = await context.new_page()
        await page.goto(url=url,timeout=30*1000)

        html_content = await page.content()

        await browser.close()

        print("Fetched HTML content:")
        print(html_content)

        with open(output_file, "w", encoding="utf-8") as file :
            file.write(html_content)

asyncio.run(main())


        