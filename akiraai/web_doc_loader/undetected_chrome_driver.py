import aiohttp
import asyncio
import random
from typing import Optional
from akiraai.web_doc_loader.scraper_framework import ScraperFramework
from akiraai.utils.logging import get_logger
from akiraai.utils.proxy_rotation import ProxyFetcher,ProxyFilter
from akiraai.web_doc_loader.scrape_do import scrape_do_fetch
from selenium.webdriver.chrome.options import Options as ChromeOptions
from concurrent.futures import ThreadPoolExecutor

from typing import List, Dict
import undetected_chromedriver as uc


logger = get_logger(name="undetected_chrome_driver_logger")

class UndetectedChromeDriverScraper(ScraperFramework):


     """
          A concrete implementation of the ScraperFramework using undetected_chromedriver.
     """

     def _configure_proxies(self) ->Optional[str]:
         """

         Configures proxy management based on the selected proxy_mode.
         This method will be invoked automatically when needed.
         Available proxy_modes: 'freeproxy', 'scrapedo', or 'none'(default) .

         """

         if self.proxy_mode == "freeproxy":

             logger.info("Freeproxy mode selected. Configuring a random free proxy.")

             proxy_filter : ProxyFilter = {
                 "anonymous":True,
                 "country_preference_set":None,
                 "outside_search":True,
                 "proxy_count": 5,
                 "secure":False,
                 "time_out":5
             }
             proxy_fetcher = ProxyFetcher(proxy_filter=proxy_filter)
             proxy_list = proxy_fetcher.validated_proxy_list()
             random_proxy =random.choice(proxy_list)
             return random_proxy
             
         elif self.proxy_mode == "scrapedo":
            logger.info("Scrape.do proxy mode selected. Will use scrape_do_fetch for requests.")                         
            return None
             
         elif self.proxy_mode == "none":
             logger.info("Proceeding without Proxy Configuration...")
             return None
             
             
         return None


     def _configure_scraper(self) ->uc.Chrome:
          
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

          #proxy management:
          proxy = self._configure_proxies()
          if self.proxy_mode == "freeproxy" and proxy:
              options.add_argument(f"--proxy-server={proxy}")
              logger.info(f"Proxy configured: {proxy}")
                                      

          try:
              return uc.Chrome(options=options)
          
          except Exception as e:
              logger.error(f"Failed to Configure the Chrome Driver: {e}")
              raise

              

     async def scrape_url_async(self, url : str) -> str:

          """
          Fetches a single URL using undetected_chromedriver.

          Args:
            url (str): The URL to fetch.

          Returns:
            str: The HTML content of the page or an error message.

          """

          driver = None
          attempt = 0
          while attempt < self.retry_limit:
            try:
                driver = self._configure_scraper()
                logger.info(f"Fetching URL: {url} (Attempt {attempt + 1})")
                driver.get(url)
                page_content = driver.page_source
                logger.info(f"Successfully scraped {url}")
                driver.quit()
                return page_content
            except Exception as e:
                attempt += 1
                logger.error(f"Error fetching {url} on attempt {attempt}: {e}")
                    
                if attempt == self.retry_limit:
                    return f"Error: Failed to fetch {url} after {self.retry_limit} attempts"
            finally:
                if driver:
                    driver.quit() 
     
     async def scrape_urls_async(self, urls: List[str]) -> Dict[str, str]:
        """
        Concurrently scrapes multiple URLs using undetected_chromedriver.

        Args:
            urls (List[str]): List of URLs to scrape.

        Returns:
            Dict[str, str]: A dictionary mapping URLs to their scraped content.
        """
        # Directly call async scrape_url_async without ThreadPoolExecutor
        tasks = [self.scrape_url_async(url) for url in urls]

    # Await the results using asyncio.gather
        results = await asyncio.gather(*tasks, return_exceptions=True)

    # Map the results to URLs
        return {url: result for url, result in zip(urls, results)}

      
         

          
          

     

      


          