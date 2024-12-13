from langchain_core.documents import Document 
from langchain_community.document_loaders.base import BaseLoader
from akiraai.utils.clean_up_html import reduce_html
from typing import Dict


class ScraperDocLoader(BaseLoader):

    """
    A custom loader to process scraper results into LangChain Documents.
    """

    def cleaned_html_dict(self, html_dict:Dict[str,str], reduction_level : int = 1) ->Dict[str, str]:

        """
        Takes a dictionary with URLs as keys and HTML content as values,
        cleans the HTML content one by one based on the reduction level.

        Args:
            html_dict (dict): Dictionary with URLs as keys and HTML content as values.
            reduction_level (int): Reduction level for cleaning HTML (0, 1, or 2).

        Returns:
            dict: A new dictionary with cleaned HTML content.
        """

        cleaned_html_dict = {}

        for url,html_content in html_dict.items():
            try:
                reduced_html = reduce_html(html_content, reduction= reduction_level)

                cleaned_html_dict[url] = reduced_html

            except Exception as e:
                cleaned_html_dict[url] = f"Error processing HTML for {url}: {e}"

        return cleaned_html_dict        

         
         
         
         
        
         