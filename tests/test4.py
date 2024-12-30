import requests

def scrape_jina_ai(url:str)->str:
  response = requests.get("https://r.jina.ai/"+ url)
  response.raise_for_status()
  return response.text

url_list = [
    "https://www.ebay.com/b/Industrial-Threadlockers/184326/bn_78213224"
]

for url in url_list:

  file_counter = 50
  markdown_content = scrape_jina_ai(url=url)
  with open(f"/workspaces/AkiraAI/Dataset/Summarization/input_markdown/raw_markdown/e-commerce/ebay/ebay_{file_counter}.md","w") as file:
    file.write(markdown_content)
    print("Saved the markdown")




