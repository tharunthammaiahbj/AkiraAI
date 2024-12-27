from akiraai.utils.html_to_markdown import markdown_conversion

with open("/workspaces/AkiraAI/tests/html_files/page_10.html","r",encoding="utf-8") as file:
    html_content = file.read()

markdown_content = markdown_conversion(html_content=html_content)

print(markdown_content)

with open("/workspaces/AkiraAI/tests/markdown_files/page_10.md","w",encoding="utf-8") as file:
    file.write(markdown_content)

print("Conversion complete. Markdown file saved")