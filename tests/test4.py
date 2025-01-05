import requests

def scrape_jina_ai(url:str)->str:
  response = requests.get("https://r.jina.ai/"+ url)
  response.raise_for_status()
  return response.text

url_list = [
    "https://www.airbnb.co.in/"
]

for url in url_list:  

  file_counter = 1
  markdown_content = scrape_jina_ai(url=url)
  with open(f"/workspaces/AkiraAI/Dataset/dataset_collection/raw_markdown/travel/airbnb/bnb_{file_counter}.md","w") as file:
    file.write(markdown_content)
    print("Saved the markdown")




