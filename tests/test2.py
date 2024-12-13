from bs4 import BeautifulSoup
import re

def segregate_and_label_html_from_file(file_path):
    # Read HTML content from file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Create labeled HTML structure
    labeled_html = []

    # Extract and label head section
    head = soup.head
    if head:
        labeled_html.append("<!-- HEAD SECTION -->")
        labeled_html.append(str(head))

    # Extract and label body section
    body = soup.body
    if body:
        labeled_html.append("<!-- BODY SECTION -->")
        labeled_html.append(str(body))

    # Extract and label links
    links = soup.find_all('a', href=True)
    if links:
        labeled_html.append("<!-- LINKS -->")
        for link in links:
            labeled_html.append(f'<a href="{link["href"]}">{link.get_text(strip=True)}</a>')

    # Extract and label images
    images = soup.find_all('img', src=True)
    if images:
        labeled_html.append("<!-- IMAGE URLS -->")
        for img in images:
            labeled_html.append(f'<img src="{img["src"]}" alt="{img.get("alt", "")}">')

    # Extract and label paragraphs
    paragraphs = soup.find_all('p')
    if paragraphs:
        labeled_html.append("<!-- PARAGRAPHS -->")
        for p in paragraphs:
            labeled_html.append(f"<p>{p.get_text(strip=True)}</p>")

    # Extract and label metadata
    metadata = soup.find_all('meta', attrs={'name': True, 'content': True})
    if metadata:
        labeled_html.append("<!-- METADATA -->")
        for meta in metadata:
            labeled_html.append(str(meta))

    # Extract and label navigation
    navigation = soup.find_all('nav')
    if navigation:
        labeled_html.append("<!-- NAVIGATION -->")
        for nav in navigation:
            labeled_html.append(str(nav))

    # Extract and label lists
    lists = soup.find_all('ul')
    if lists:
        labeled_html.append("<!-- LISTS -->")
        for ul in lists:
            labeled_html.append(str(ul))

    # Extract and label tables
    tables = soup.find_all('table')
    if tables:
        labeled_html.append("<!-- TABLES -->")
        for table in tables:
            labeled_html.append(str(table))

    # Remove unwanted tags globally
    for tag in soup(['script', 'style', 'iframe', 'noscript']):
        tag.decompose()

    # Join all parts into a single HTML string with labels
    cleaned_and_labeled_html = "\n".join(labeled_html)

    return cleaned_and_labeled_html


# Process the HTML file
input_file_path = '/workspaces/AkiraAI/tests/html_samples/amazon/output1.html'  # Replace with your file path
output_file_path = 'segregated.html'

labeled_html = segregate_and_label_html_from_file(input_file_path)

# Save the labeled HTML to a new file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(labeled_html)

print(f"Labeled HTML has been saved to {output_file_path}")
