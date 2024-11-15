from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://playwright.dev")
    html_content = page.content()  # Get the HTML content of the page
    print(html_content)  # Print the HTML content
    browser.close()
