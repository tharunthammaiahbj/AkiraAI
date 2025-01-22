import re
from bs4 import BeautifulSoup, Comment, element, Tag, NavigableString
from akiraai.html2text import CustomHTML2Text, html2text
from urllib.parse import urlparse


class InvalidCSSSelectorError(Exception):
    pass

MIN_WORD_THRESHOLD = 1

def sanitize_html(html: str) -> str:
    """
    Sanitize an HTML string by escaping quotes and removing unwanted characters.

    Args:
        html (str): The HTML string to sanitize.

    Returns:
        str: The sanitized HTML string.
    """
    # Escape all double and single quotes
    sanitized_html = html.replace('"', '\\"').replace("'", "\\'")

    # (Optional) Replace any unwanted characters (uncomment to enable)
    # sanitized_html = re.sub(r'[^\w\s.,;:!?=\[\]{}()<>\/\\\-"]', '', sanitized_html)

    return sanitized_html

def sanitize_input_encode(text: str) -> str:
    """Sanitize input to handle potential encoding issues."""
    try:
        try:
            if not text:
                return ''
            # Attempt to encode and decode as UTF-8 to handle potential encoding issues
            return text.encode('utf-8', errors='ignore').decode('utf-8')
        except UnicodeEncodeError as e:
            print(f"Warning: Encoding issue detected. Some characters may be lost. Error: {e}")
            # Fall back to ASCII if UTF-8 fails
            return text.encode('ascii', errors='ignore').decode('ascii')
    except Exception as e:
        raise ValueError(f"Error sanitizing input: {str(e)}") from e
    
def replace_inline_tags(soup, tags, only_text=False):
    """
    Replace inline HTML tags with Markdown-style equivalents.

    How it works:
    1. Maps specific tags (e.g., <b>, <i>) to Markdown syntax.
    2. Finds and replaces all occurrences of these tags in the provided BeautifulSoup object.
    3. Optionally replaces tags with their text content only.

    Args:
        soup (BeautifulSoup): Parsed HTML content.
        tags (List[str]): List of tags to replace.
        only_text (bool): Whether to replace tags with plain text. Defaults to False.

    Returns:
        BeautifulSoup: Updated BeautifulSoup object with replaced tags.
    """

    tag_replacements = {
        'b': lambda tag: f"**{tag.text}**",
        'i': lambda tag: f"*{tag.text}*",
        'u': lambda tag: f"__{tag.text}__",
        'span': lambda tag: f"{tag.text}",
        'del': lambda tag: f"~~{tag.text}~~",
        'ins': lambda tag: f"++{tag.text}++",
        'sub': lambda tag: f"~{tag.text}~",
        'sup': lambda tag: f"^^{tag.text}^^",
        'strong': lambda tag: f"**{tag.text}**",
        'em': lambda tag: f"*{tag.text}*",
        'code': lambda tag: f"`{tag.text}`",
        'kbd': lambda tag: f"`{tag.text}`",
        'var': lambda tag: f"_{tag.text}_",
        's': lambda tag: f"~~{tag.text}~~",
        'q': lambda tag: f'"{tag.text}"',
        'abbr': lambda tag: f"{tag.text} ({tag.get('title', '')})",
        'cite': lambda tag: f"_{tag.text}_",
        'dfn': lambda tag: f"_{tag.text}_",
        'time': lambda tag: f"{tag.text}",
        'small': lambda tag: f"<small>{tag.text}</small>",
        'mark': lambda tag: f"=={tag.text}=="
    }
    
    replacement_data = [(tag, tag_replacements.get(tag, lambda t: t.text)) for tag in tags]

    for tag_name, replacement_func in replacement_data:
        for tag in soup.find_all(tag_name):
            replacement_text = tag.text if only_text else replacement_func(tag)
            tag.replace_with(replacement_text)

    return soup    

    # for tag_name in tags:
    #     for tag in soup.find_all(tag_name):
    #         if not only_text:
    #             replacement_text = tag_replacements.get(tag_name, lambda t: t.text)(tag)
    #             tag.replace_with(replacement_text)
    #         else:
    #             tag.replace_with(tag.text)

    # return soup


def extract_metadata(html, soup=None):
    """
    Extract optimized content, media, and links from website HTML.

    How it works:
    1. Similar to `get_content_of_website`, but optimized for performance.
    2. Filters and scores images for usefulness.
    3. Extracts contextual descriptions for media files.
    4. Handles excluded tags and CSS selectors.
    5. Cleans HTML and converts it to Markdown.

    Args:
        url (str): The website URL.
        html (str): The HTML content of the website.
        word_count_threshold (int): Minimum word count for content inclusion. Defaults to MIN_WORD_THRESHOLD.
        css_selector (Optional[str]): CSS selector to extract specific content. Defaults to None.
        **kwargs: Additional options for customization.

    Returns:
        Dict[str, Any]: Extracted content including Markdown, cleaned HTML, media, links, and metadata.
    """
    
    metadata = {}
    
    if not html and not soup:
        return {}
    
    if not soup:
        soup = BeautifulSoup(html, 'lxml')
    
    head = soup.head
    if not head:
        return metadata
    
    # Title
    title_tag = head.find('title')
    metadata['title'] = title_tag.string.strip() if title_tag and title_tag.string else None

    # Meta description
    description_tag = head.find('meta', attrs={'name': 'description'})
    metadata['description'] = description_tag.get('content', '').strip() if description_tag else None

    # Meta keywords
    keywords_tag = head.find('meta', attrs={'name': 'keywords'})
    metadata['keywords'] = keywords_tag.get('content', '').strip() if keywords_tag else None

    # Meta author
    author_tag = head.find('meta', attrs={'name': 'author'})
    metadata['author'] = author_tag.get('content', '').strip() if author_tag else None

    # Open Graph metadata
    og_tags = head.find_all('meta', attrs={'property': re.compile(r'^og:')})
    for tag in og_tags:
        property_name = tag.get('property', '').strip()
        content = tag.get('content', '').strip()
        if property_name and content:
            metadata[property_name] = content

    # Twitter Card metadata
    twitter_tags = head.find_all('meta', attrs={'name': re.compile(r'^twitter:')})
    for tag in twitter_tags:
        property_name = tag.get('name', '').strip()
        content = tag.get('content', '').strip()
        if property_name and content:
            metadata[property_name] = content
    
    return metadata


def get_content_of_website(url, html, word_count_threshold = MIN_WORD_THRESHOLD, css_selector = None, **kwargs):
    """
    Extract structured content, media, and links from website HTML.

    How it works:
    1. Parses the HTML content using BeautifulSoup.
    2. Extracts internal/external links and media (images, videos, audios).
    3. Cleans the content by removing unwanted tags and attributes.
    4. Converts cleaned HTML to Markdown.
    5. Collects metadata and returns the extracted information.

    Args:
        url (str): The website URL.
        html (str): The HTML content of the website.
        word_count_threshold (int): Minimum word count for content inclusion. Defaults to MIN_WORD_THRESHOLD.
        css_selector (Optional[str]): CSS selector to extract specific content. Defaults to None.

    Returns:
        Dict[str, Any]: Extracted content including Markdown, cleaned HTML, media, links, and metadata.
    """

    try:
        if not html:
            return None
        # Parse HTML content with BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # Get the content within the <body> tag
        body = soup.body
        
        # If css_selector is provided, extract content based on the selector
        if css_selector:
            selected_elements = body.select(css_selector)
            if not selected_elements:
                raise InvalidCSSSelectorError(f"Invalid CSS selector , No elements found for CSS selector: {css_selector}")
            div_tag = soup.new_tag('div')
            for el in selected_elements:
                div_tag.append(el)
            body = div_tag
            
        links = {
            'internal': [],
            'external': []
        }
        
        # Extract all internal and external links
        for a in body.find_all('a', href=True):
            href = a['href']
            url_base = url.split('/')[2]
            if href.startswith('http') and url_base not in href:
                links['external'].append({
                    'href': href,
                    'text': a.get_text()
                })
            else:
                links['internal'].append(
                    {
                        'href': href,
                        'text': a.get_text()
                    }
                )

        # Remove script, style, and other tags that don't carry useful content from body
        for tag in body.find_all(['script', 'style', 'link', 'meta', 'noscript']):
            tag.decompose()

        # Remove all attributes from remaining tags in body, except for img tags
        for tag in body.find_all():
            if tag.name != 'img':
                tag.attrs = {}

        # Extract all img tgas int0 [{src: '', alt: ''}]
        media = {
            'images': [],
            'videos': [],
            'audios': []
        }
        for img in body.find_all('img'):
            media['images'].append({
                'src': img.get('src'),
                'alt': img.get('alt'),
                "type": "image"
            })
            
        # Extract all video tags into [{src: '', alt: ''}]
        for video in body.find_all('video'):
            media['videos'].append({
                'src': video.get('src'),
                'alt': video.get('alt'),
                "type": "video"
            })
            
        # Extract all audio tags into [{src: '', alt: ''}]
        for audio in body.find_all('audio'):
            media['audios'].append({
                'src': audio.get('src'),
                'alt': audio.get('alt'),
                "type": "audio"
            })
        
        # Replace images with their alt text or remove them if no alt text is available
        for img in body.find_all('img'):
            alt_text = img.get('alt')
            if alt_text:
                img.replace_with(soup.new_string(alt_text))
            else:
                img.decompose()


        # Create a function that replace content of all"pre" tag with its inner text
        def replace_pre_tags_with_text(node):
            for child in node.find_all('pre'):
                # set child inner html to its text
                child.string = child.get_text()
            return node
        
        # Replace all "pre" tags with their inner text
        body = replace_pre_tags_with_text(body)
        
        # Replace inline tags with their text content
        body = replace_inline_tags(
            body, 
            ['b', 'i', 'u', 'span', 'del', 'ins', 'sub', 'sup', 'strong', 'em', 'code', 'kbd', 'var', 's', 'q', 'abbr', 'cite', 'dfn', 'time', 'small', 'mark'],
            only_text=kwargs.get('only_text', False)
        )

        # Recursively remove empty elements, their parent elements, and elements with word count below threshold
        def remove_empty_and_low_word_count_elements(node, word_count_threshold):
            for child in node.contents:
                if isinstance(child, element.Tag):
                    remove_empty_and_low_word_count_elements(child, word_count_threshold)
                    word_count = len(child.get_text(strip=True).split())
                    if (len(child.contents) == 0 and not child.get_text(strip=True)) or word_count < word_count_threshold:
                        child.decompose()
            return node

        body = remove_empty_and_low_word_count_elements(body, word_count_threshold)
        
        def remove_small_text_tags(body: Tag, word_count_threshold: int = MIN_WORD_THRESHOLD):
            # We'll use a list to collect all tags that don't meet the word count requirement
            tags_to_remove = []

            # Traverse all tags in the body
            for tag in body.find_all(True):  # True here means all tags
                # Check if the tag contains text and if it's not just whitespace
                if tag.string and tag.string.strip():
                    # Split the text by spaces and count the words
                    word_count = len(tag.string.strip().split())
                    # If the word count is less than the threshold, mark the tag for removal
                    if word_count < word_count_threshold:
                        tags_to_remove.append(tag)

            # Remove all marked tags from the tree
            for tag in tags_to_remove:
                tag.decompose()  # or tag.extract() to remove and get the element

            return body
        
    
        # Remove small text tags
        body = remove_small_text_tags(body, word_count_threshold)       
        
        def is_empty_or_whitespace(tag: Tag):
            if isinstance(tag, NavigableString):
                return not tag.strip()
            # Check if the tag itself is empty or all its children are empty/whitespace
            if not tag.contents:
                return True
            return all(is_empty_or_whitespace(child) for child in tag.contents)

        def remove_empty_tags(body: Tag):
            # Continue processing until no more changes are made
            changes = True
            while changes:
                changes = False
                # Collect all tags that are empty or contain only whitespace
                empty_tags = [tag for tag in body.find_all(True) if is_empty_or_whitespace(tag)]
                for tag in empty_tags:
                    # If a tag is empty, decompose it
                    tag.decompose()
                    changes = True  # Mark that a change was made

            return body        

        
        # Remove empty tags
        body = remove_empty_tags(body)
        
        # Flatten nested elements with only one child of the same type
        def flatten_nested_elements(node):
            for child in node.contents:
                if isinstance(child, element.Tag):
                    flatten_nested_elements(child)
                    if len(child.contents) == 1 and child.contents[0].name == child.name:
                        # print('Flattening:', child.name)
                        child_content = child.contents[0]
                        child.replace_with(child_content)
                        
            return node

        body = flatten_nested_elements(body)
        


        # Remove comments
        for comment in soup.find_all(string=lambda text: isinstance(text, Comment)): 
            comment.extract()

        # Remove consecutive empty newlines and replace multiple spaces with a single space
        cleaned_html = str(body).replace('\n\n', '\n').replace('  ', ' ')
        
        # Sanitize the cleaned HTML content
        cleaned_html = sanitize_html(cleaned_html)
        # sanitized_html = escape_json_string(cleaned_html)

        # Convert cleaned HTML to Markdown
        h = html2text.HTML2Text()
        h = CustomHTML2Text()
        h.ignore_links = True
        markdown = h.handle(cleaned_html)
        markdown = markdown.replace('    ```', '```')
            
        try:
            meta = extract_metadata(html, soup)
        except Exception as e:
            print('Error extracting metadata:', str(e))
            meta = {}
                
        
        # Return the Markdown content
        return{
            'markdown': markdown,
            'cleaned_html': cleaned_html,
            'success': True,
            'media': media,
            'links': links,
            'metadata': meta
        }

    except Exception as e:
        print('Error processing HTML content:', str(e))
        raise InvalidCSSSelectorError(f"Invalid CSS selector: {css_selector}") from e

def fast_format_html(html_string):
    """
    A fast HTML formatter that uses string operations instead of parsing.
    
    Args:
        html_string (str): The HTML string to format
        
    Returns:
        str: The formatted HTML string
    """
    # Initialize variables
    indent = 0
    indent_str = "  "  # Two spaces for indentation
    formatted = []
    in_content = False
    
    # Split by < and > to separate tags and content
    parts = html_string.replace('>', '>\n').replace('<', '\n<').split('\n')
    
    for part in parts:
        if not part.strip():
            continue
            
        # Handle closing tags
        if part.startswith('</'):
            indent -= 1
            formatted.append(indent_str * indent + part)
            
        # Handle self-closing tags
        elif part.startswith('<') and part.endswith('/>'):
            formatted.append(indent_str * indent + part)
            
        # Handle opening tags
        elif part.startswith('<'):
            formatted.append(indent_str * indent + part)
            indent += 1
            
        # Handle content between tags
        else:
            content = part.strip()
            if content:
                formatted.append(indent_str * indent + content)
    
    return '\n'.join(formatted)


def normalize_url(href, base_url):
    """Normalize URLs to ensure consistent format"""
    from urllib.parse import urljoin, urlparse

    # Parse base URL to get components
    parsed_base = urlparse(base_url)
    if not parsed_base.scheme or not parsed_base.netloc:
        raise ValueError(f"Invalid base URL format: {base_url}")

    # Use urljoin to handle all cases
    normalized = urljoin(base_url, href.strip())
    return normalized

def is_external_url(url: str, base_domain: str) -> bool:
    """
    Extract the base domain from a given URL, handling common edge cases.

    How it works:
    1. Parses the URL to extract the domain.
    2. Removes the port number and 'www' prefix.
    3. Handles special domains (e.g., 'co.uk') to extract the correct base.

    Args:
        url (str): The URL to extract the base domain from.

    Returns:
        str: The extracted base domain or an empty string if parsing fails.
    """
    special = {'mailto:', 'tel:', 'ftp:', 'file:', 'data:', 'javascript:'}
    if any(url.lower().startswith(p) for p in special):
        return True
        
    try:
        parsed = urlparse(url)
        if not parsed.netloc:  # Relative URL
            return False
            
        # Strip 'www.' from both domains for comparison
        url_domain = parsed.netloc.lower().replace('www.', '')
        base = base_domain.lower().replace('www.', '')
        
        # Check if URL domain ends with base domain
        return not url_domain.endswith(base)
    except Exception:
        return False


def get_base_domain(url: str) -> str:
    """
    Extract the base domain from a given URL, handling common edge cases.

    How it works:
    1. Parses the URL to extract the domain.
    2. Removes the port number and 'www' prefix.
    3. Handles special domains (e.g., 'co.uk') to extract the correct base.

    Args:
        url (str): The URL to extract the base domain from.

    Returns:
        str: The extracted base domain or an empty string if parsing fails.
    """
    try:
        # Get domain from URL
        domain = urlparse(url).netloc.lower()
        if not domain:
            return ""
            
        # Remove port if present
        domain = domain.split(':')[0]
        
        # Remove www
        domain = re.sub(r'^www\.', '', domain)
        
        # Extract last two parts of domain (handles co.uk etc)
        parts = domain.split('.')
        if len(parts) > 2 and parts[-2] in {
            'co', 'com', 'org', 'gov', 'edu', 'net', 
            'mil', 'int', 'ac', 'ad', 'ae', 'af', 'ag'
        }:
            return '.'.join(parts[-3:])
            
        return '.'.join(parts[-2:])
    except Exception:
        return ""