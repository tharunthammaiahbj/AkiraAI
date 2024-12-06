from akiraai.web_doc_loader.scraper_framework import ScraperFramework
from akiraai.utils.logging import get_logger
from selenium.webdriver.chrome.options import Options as ChromeOptions
import aiohttp
import asyncio
from typing import List, Dict
import undetected_chromedriver as uc


logger = get_logger(name="undetected_chrome_driver_logger")

class UndetectedChromeDriverScraper(ScraperFramework):


     """
          A concrete implementation of the ScraperFramework using undetected_chromedriver.
     """

     def _configure_driver(self) ->uc.Chrome:
          
          """
           Configures and returns an instance of the Chrome driver with optional proxy settings.
           Returns:
            uc.Chrome: Configured Chrome driver instance.

          """

          options = ChromeOptions()
          options.headless = self.headless


          options.add_argument("--disable-blink-features=AutomationControlled")
          options.add_argument("--no-sandbox")
          options.add_argument("--disable-dev-shm-usage")

          return uc.Chrome(options=options)

     async def scrape_urls_async(self, urls):
          pass
          

     

      


          