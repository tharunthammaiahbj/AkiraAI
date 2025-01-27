from akiraai.celery_tasks.html_to_clean_markdown_async import process_html_to_markdown


with open("/workspaces/AkiraAI/tests/sample_htmls/ebay1_html.html","r") as f:
    raw_html = f.read()

url = "https://www.ebay.com/b/Womens-Clothing-Shoes-Accessories/260010/bn_7116391826"

# Submit the task
result = process_html_to_markdown.delay(url, raw_html)

# Print task ID
print(f"Task ID: {result.id}")