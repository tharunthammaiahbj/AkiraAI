"""
Conversion of HTML to Markdown 

"""
from markdownify import markdownify

def markdown_conversion(html_content:str) ->str:
    """
    Argument: 
        html_content: cleaned_html
    returns :
        cleaned and formatted Markdown

    """
    if not html_content:
        raise ValueError("Input HTML content cannot be empty.")

    markdown_content = markdownify(html_content)

    return markdown_content

