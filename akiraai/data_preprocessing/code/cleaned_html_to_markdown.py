from akiraai.data_preprocessing.code.cleaned_html_conversion import clean_html_conversion
from akiraai.utils.markdown_generation_strategy import DefaultMarkdownGenerator
from akiraai.utils.html_utils import sanitize_input_encode
import time

with open("/workspaces/AkiraAI/tests/sample_htmls/ebay1_html.html","r") as f:
    raw_html = f.read()

url = "https://www.ebay.com/b/Womens-Clothing-Shoes-Accessories/260010/bn_7116391826"

result = clean_html_conversion(
    html= raw_html,
    url= url
)

cleaned_html = sanitize_input_encode(result.get("cleaned_html", ""))
fit_markdown = sanitize_input_encode(result.get("fit_markdown", ""))
fit_html = sanitize_input_encode(result.get("fit_html", ""))
media = result.get("media", [])
links = result.get("links", [])
metadata = result.get("metadata", {})

markdown_generator = DefaultMarkdownGenerator()
markdown_result = markdown_generator.generate_markdown(
    cleaned_html=cleaned_html,
    base_url=url,
)
markdown_v2 = markdown_result
markdown = sanitize_input_encode(markdown_result.raw_markdown)

processing_time = int((time.perf_counter() - time.perf_counter()) * 1000)
print(f"Processed {url} in {processing_time}ms")

markdown_file_path = "/workspaces/AkiraAI/tests/sample_markdowns/example.md"
with open(markdown_file_path, "w", encoding="utf-8") as md_file:
    md_file.write(markdown)
