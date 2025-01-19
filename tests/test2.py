from akiraai.data_preprocessing.clean_up_html import cleanup_html, minify_html, reduce_html


# Read the raw HTML content from a file
with open("/workspaces/AkiraAI/tests/sample_htmls/ebay1_html.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Clean up the HTML and extract relevant information
title, body_content, links_urls, image_urls = cleanup_html(
    html_content=html_content,
    base_url="https://ebay.com"
)

# Reduce the cleaned HTML for further optimization
reduced_html = reduce_html(html=html_content, reduction=1)

# Save the cleaned and minified HTML to a file
with open("/workspaces/AkiraAI/tests/sample_clean_htmls/cleaned_amazon1_html.html", "w", encoding="utf-8") as file:
    file.write(reduced_html)

# Convert the final cleaned HTML to Markdown using markdownify
markdown_content = md(reduced_html).strip()

# Save the Markdown content to a file
with open("/workspaces/AkiraAI/tests/sample_markdowns/cleaned_amazon1_md.md", "w", encoding="utf-8") as file:
    file.write(markdown_content)

# Print confirmation (optional)
print(f"Markdown saved to /workspaces/AkiraAI/tests/sample_markdowns/cleaned_amazon1_md.md")
