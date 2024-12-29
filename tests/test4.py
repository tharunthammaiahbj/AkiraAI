import requests

def scrape_jina_ai(url:str)->str:
  response = requests.get("https://r.jina.ai/"+ url)
  response.raise_for_status()
  return response.text

url = "https://en.wikipedia.org/wiki/Orange"

markdown_content = scrape_jina_ai(url=url)

print(markdown_content)



