import time
from typing import Dict
from akiraai.utils.html_utils import sanitize_html, sanitize_input_encode
from akiraai.utils.markdown_generation_strategy import DefaultMarkdownGenerator

def process_html_to_markdown(html: str, verbose: bool = False) -> Dict:
    """
    Convert raw HTML content to clean Markdown.

    Args:
        html (str): Raw HTML content to be converted.
        verbose (bool): Whether to enable verbose logging.

    Returns:
        dict: Processed result containing cleaned HTML, Markdown, and related data.
    """
    t1 = time.perf_counter()

    try:
        # Step 1: Clean the HTML (sanitize input HTML)
        cleaned_html = sanitize_html(html)

        # Step 2: Generate Markdown from the cleaned HTML
        markdown_generator = DefaultMarkdownGenerator()
        markdown_result = markdown_generator.generate_markdown(cleaned_html=cleaned_html)

        # Step 3: Prepare the result
        result = {
            "cleaned_html": cleaned_html,
            "markdown": sanitize_input_encode(markdown_result.raw_markdown),
            "markdown_v2": sanitize_input_encode(markdown_result.raw_markdown),  # Assuming markdown_v2 is the same for now
            "fit_markdown": sanitize_input_encode(markdown_result.fit_markdown),
            "fit_html": sanitize_input_encode(markdown_result.fit_html),
            "media": markdown_result.media,
            "links": markdown_result.links,
            "metadata": markdown_result.metadata,
            "success": True,
            "error_message": "",
            "timing": int((time.perf_counter() - t1) * 1000)  # Time in milliseconds
        }

        # Optional verbose logging
        if verbose:
            print(f"Processed HTML to Markdown | Time: {result['timing']}ms")

        return result

    except Exception as e:
        return {
            "success": False,
            "error_message": f"Error processing HTML to Markdown: {str(e)}",
            "timing": int((time.perf_counter() - t1) * 1000)
        }

def convert_html_file_to_markdown(input_file: str, output_file: str, verbose: bool = False):
    """
    Read HTML from an input file, convert it to Markdown, and write the output to a file.

    Args:
        input_file (str): Path to the input HTML file.
        output_file (str): Path to the output Markdown file.
        verbose (bool): Whether to enable verbose logging.
    """
    try:
        # Read the HTML content from the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Convert HTML to Markdown
        result = process_html_to_markdown(html_content, verbose)

        # Check if conversion was successful
        if result['success']:
            # Write the Markdown output to the file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(result['markdown'])
            print(f"Markdown saved to {output_file}")
        else:
            print(f"Error: {result['error_message']}")

    except Exception as e:
        print(f"Error reading or writing files: {str(e)}")

# Example usage
input_html_file = '/workspaces/AkiraAI/tests/sample_htmls/amazon_html1.html'  # Input HTML file
output_markdown_file = '/workspaces/AkiraAI/tests/sample_markdowns/cleaned_amazon1_md.md'  # Output Markdown file

convert_html_file_to_markdown(input_html_file, output_markdown_file, verbose=True)
