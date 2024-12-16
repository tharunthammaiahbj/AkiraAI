from langchain_core.documents import Document
from bs4 import BeautifulSoup


def doc_converter(url: str, cleaned_html: str) -> Document:

    """
    Converts Cleaned HTML to Langchain Document Format. 
    """
    soup = BeautifulSoup(cleaned_html, 'html.parser')

    title_tag = soup.find('title')
    title = title_tag.get_text() if title_tag else ""

    return Document(page_content=cleaned_html, metadata = {'source': url, 'title':title})
