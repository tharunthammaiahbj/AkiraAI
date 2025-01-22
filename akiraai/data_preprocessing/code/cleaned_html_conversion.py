from bs4 import BeautifulSoup
from akiraai.utils.html_utils import get_base_domain
from akiraai.utils.html_utils import extract_metadata
from akiraai.utils.html_functions import process_element, process_image, flatten_nested_elements
from akiraai.utils.logging import get_logger
from typing import Dict, Any
import re

logger = get_logger(name="html_conversion_logger")

MIN_WORD_THRESHOLD = 1
SOCIAL_MEDIA_DOMAINS = [
                            'facebook.com',
                            'twitter.com',
                            'x.com',
                            'linkedin.com',
                            'instagram.com',
                            'pinterest.com',
                            'tiktok.com',
                            'snapchat.com',
                            'reddit.com',
                        ]


def clean_html_conversion(url: str, html: str, word_count_threshold: int = MIN_WORD_THRESHOLD, css_selector: str = None, **kwargs) -> Dict[str, Any]:
        """
        Extract content from HTML using BeautifulSoup.

        Args:
            url (str): The URL of the page to scrape.
            html (str): The HTML content of the page to scrape.
            word_count_threshold (int): The minimum word count threshold for content extraction.
            css_selector (str): The CSS selector to use for content extraction.
            **kwargs: Additional keyword arguments.

        Returns:
            dict: A dictionary containing the extracted content.
        """
        success = True
        if not html:
            return None

        parser_type = kwargs.get('parser', 'lxml')
        soup = BeautifulSoup(html, parser_type)
        body = soup.body
        base_domain = get_base_domain(url)
        
        try:
            meta = extract_metadata("", soup)
        except Exception as e:
            logger.error(f"Error extracting metadata:{e}")          
            meta = {}
        
        # Handle tag-based removal first - faster than CSS selection
        excluded_tags = set(kwargs.get('excluded_tags', []) or [])  
        if excluded_tags:
            for element in body.find_all(lambda tag: tag.name in excluded_tags):
                element.extract()
        
        # Handle CSS selector-based removal
        excluded_selector = kwargs.get('excluded_selector', '')
        if excluded_selector:
            is_single_selector = ',' not in excluded_selector and ' ' not in excluded_selector
            if is_single_selector:
                while element := body.select_one(excluded_selector):
                    element.extract()
            else:
                for element in body.select(excluded_selector):
                    element.extract()  
        
        if css_selector:
            selected_elements = body.select(css_selector)
            if not selected_elements:
                return {
                    'markdown': '',
                    'cleaned_html': '',
                    'success': True,
                    'media': {'images': [], 'videos': [], 'audios': []},
                    'links': {'internal': [], 'external': []},
                    'metadata': {},
                    'message': f"No elements found for CSS selector: {css_selector}"
                }
                # raise InvalidCSSSelectorError(f"Invalid CSS selector, No elements found for CSS selector: {css_selector}")
            body = soup.new_tag('div')
            for el in selected_elements:
                body.append(el)

        kwargs['exclude_social_media_domains'] = set(kwargs.get('exclude_social_media_domains', []) + SOCIAL_MEDIA_DOMAINS)
        kwargs['exclude_domains'] = set(kwargs.get('exclude_domains', []))
        if kwargs.get('exclude_social_media_links', False):
            kwargs['exclude_domains'] = kwargs['exclude_domains'].union(kwargs['exclude_social_media_domains'])
        
        result_obj = process_element(
            url, 
            body, 
            word_count_threshold = word_count_threshold, 
            base_domain=base_domain,
            **kwargs
        )
        
        links = {'internal': [], 'external': []}
        media = result_obj['media']
        internal_links_dict = result_obj['internal_links_dict']
        external_links_dict = result_obj['external_links_dict']
        
        # Update the links dictionary with unique links
        links['internal'] = list(internal_links_dict.values())
        links['external'] = list(external_links_dict.values())

        # # Process images using ThreadPoolExecutor
        imgs = body.find_all('img')
        
        media['images'] = [
            img for result in (process_image(img, url, i, len(imgs)) 
                            for i, img in enumerate(imgs))
            if result is not None
            for img in result
        ]

        body = flatten_nested_elements(body)
        base64_pattern = re.compile(r'data:image/[^;]+;base64,([^"]+)')
        for img in imgs:
            src = img.get('src', '')
            if base64_pattern.match(src):
                # Replace base64 data with empty string
                img['src'] = base64_pattern.sub('', src)
                
        str_body = ""
        try:
            str_body = body.encode_contents().decode('utf-8')
        except Exception as e:
            # Reset body to the original HTML
            success = False
            body = BeautifulSoup(html, 'html.parser')
            
            # Create a new div with a special ID
            error_div = body.new_tag('div', id='crawl4ai_error_message')
            error_div.string = '''
            Crawl4AI Error: This page is not fully supported.
            
            Possible reasons:
            1. The page may have restrictions that prevent crawling.
            2. The page might not be fully loaded.
            
            Suggestions:
            - Try calling the crawl function with these parameters:
            magic=True,
            - Set headless=False to visualize what's happening on the page.
            
            If the issue persists, please check the page's structure and any potential anti-crawling measures.
            '''
            
            # Append the error div to the body
            body.body.append(error_div)
            str_body = body.encode_contents().decode('utf-8')
            
            print(f"[LOG] 😧 Error: After processing the crawled HTML and removing irrelevant tags, nothing was left in the page. Check the markdown for further details.")
            logger.error("After processing the crawled HTML and removing irrelevant tags, nothing was left in the page. Check the markdown for further details.")

        cleaned_html = str_body.replace('\n\n', '\n').replace('  ', ' ')

        
        return {
            # **markdown_content,
            'cleaned_html': cleaned_html,
            'success': success,
            'media': media,
            'links': links,
            'metadata': meta
        }