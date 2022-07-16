#twitter : mrirfan___07
#instagram : mrirfan___07

import requests
import json
# go to this side https://newsapi.org/ copy the api end paste  here this site
url=requests.get("https://newsapi.org/v2/everything?q=india&from=2022-07-15&to=2022-07-15&sortBy=popularity&apiKey=<Enter api key>")
loding=json.loads(url.text)

news=1
for find in loding['articles']:
	print(f"todays news {news}")
	print(f"title: {find['title']}")
	print(f"description: {find['description']}")
	print(f"content: {find['content']}")
	print()
	print("------------------------------------***------------------------------------")

	news+=1
