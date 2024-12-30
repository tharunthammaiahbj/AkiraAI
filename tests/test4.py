import requests

def scrape_jina_ai(url:str)->str:
  response = requests.get("https://r.jina.ai/"+ url)
  response.raise_for_status()
  return response.text

url_list = [
    "https://sale.alibaba.com/p/rank/detail.html?spm=a27aq.rank_detail.6622646540.32.50c243bfiwWgnu&wx_navbar_transparent=true&cardType=101002747&cardId=201334614&topOfferIds=&templateBusinessCode=&bucket=undefined"
]

for url in url_list:

  file_counter = 11
  markdown_content = scrape_jina_ai(url=url)
  with open(f"/workspaces/AkiraAI/Dataset/Summarization/input_markdown/raw_markdown/e-commerce/alibaba/ali_{file_counter}.md","w") as file:
    file.write(markdown_content)
    print("Saved the markdown")




