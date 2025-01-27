from celery_app import app
from akiraai.data_preprocessing.code.cleaned_html_conversion import clean_html_conversion
from akiraai.utils.markdown_generation_strategy import DefaultMarkdownGenerator
from akiraai.utils.html_utils import sanitize_input_encode
import time

@app.task
def process_html_to_markdown(url, raw_html):
    """
    Celery task to process HTML content and generate Markdown.
    
    Args:
        url (str): The URL of the webpage.
        raw_html (str): The raw HTML content to process.
    
    Returns:
        dict: Contains processed Markdown, metadata, media links, and processing time.
    """
    try:
        start_time = time.perf_counter()

        # Process HTML
        result = clean_html_conversion(html=raw_html, url=url)

        # Extract processed results
        cleaned_html = sanitize_input_encode(result.get("cleaned_html", ""))
        fit_markdown = sanitize_input_encode(result.get("fit_markdown", ""))
        fit_html = sanitize_input_encode(result.get("fit_html", ""))
        media = result.get("media", [])
        links = result.get("links", [])
        metadata = result.get("metadata", {})

        # Generate Markdown
        markdown_generator = DefaultMarkdownGenerator()
        markdown_result = markdown_generator.generate_markdown(
            cleaned_html=cleaned_html,
            base_url=url,
        )
        markdown_v2 = markdown_result
        markdown = sanitize_input_encode(markdown_result.raw_markdown)

        # Calculate processing time
        processing_time = int((time.perf_counter() - start_time) * 1000)

        # Return results
        return {
            "url": url,
            "markdown": markdown,
            "markdown_v2": markdown_v2,
            "metadata": metadata,
            "media": media,
            "links": links,
            "processing_time_ms": processing_time,
        }

    except Exception as e:
        # Log the error and raise it
        app.logger.error(f"Error processing {url}: {e}")
        raise

