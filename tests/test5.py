from akiraai.utils.markdown_result_gen import MarkdownGenerationResult
from akiraai.html2text import CustomHTML2Text
from akiraai.utils.markdown_generation_strategy import DefaultMarkdownGenerator  # Adjust this import path to where your DefaultMarkdownGenerator is

# Path to your HTML file
html_file_path = "/workspaces/AkiraAI/tests/sample_htmls/amazon_html1.html"

# Read the HTML content
with open(html_file_path, "r", encoding="utf-8") as f:
    cleaned_html = f.read()

# Initialize the markdown generator
markdown_generator = DefaultMarkdownGenerator()

# Generate the markdown (no content filtering)
markdown_result: MarkdownGenerationResult = markdown_generator.generate_markdown(cleaned_html, citations=True)

# Print the raw markdown result
print("Raw Markdown:\n", markdown_result.raw_markdown)

with open("/workspaces/AkiraAI/tests/sample_markdowns/cleaned_amazon1_md.md", "w", encoding="utf-8") as f:
    f.write(markdown_result.raw_markdown)

# Print markdown with citations (if citations are enabled)
print("\nMarkdown with Citations:\n", markdown_result.markdown_with_citations)

# Print references markdown (if citations are enabled)
print("\nReferences Markdown:\n", markdown_result.references_markdown)
