import requests

def scrape_jina_ai(url:str)->str:
  response = requests.get("https://r.jina.ai/"+ url)
  response.raise_for_status()
  return response.text

url_list = [
   

]

for url in url_list:

  file_counter = 43
  markdown_content = scrape_jina_ai(url=url)
  with open(f"/workspaces/AkiraAI/Dataset/Summarization/input_markdown/raw_markdown/e-commerce/com_{file_counter}.md","w") as file:
    file.write(markdown_content)
    print("Saved the markdown")




