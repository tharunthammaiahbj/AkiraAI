from playwright.sync_api import sync_playwright

def check_playwright_and_chromium():
    try:
        # Start Playwright in sync mode
        with sync_playwright() as p:
            # Try to launch Chromium browser
            browser = p.chromium.launch()
            print("Playwright and Chromium are installed correctly!")
            browser.close()
    except Exception as e:
        print("Error:", str(e))
        print("Playwright or Chromium might not be installed correctly!")

# Run the check
check_playwright_and_chromium()
