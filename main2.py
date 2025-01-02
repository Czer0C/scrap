# https://hotgear.vn/collections/vga-card-man-hinh

import os
import json
from scrapegraphai.graphs import SmartScraperGraph
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

# Define the configuration for the scraping pipeline
graph_config = {
    "llm": {
        "api_key": api_key,
        "model": "openai/gpt-4o-mini",
    },
    "verbose": True,
    "headless": False,
}

page_pattern = "https://hotgear.vn/collections/vga-card-man-hinh?q=filter=((collectionid:product=1001473971))&page="

list_pages = [page_pattern + str(i) for i in range(1, 56)]

print(list_pages)

arr_all = []

for page in list_pages:
	
  smart_scraper_graph = SmartScraperGraph(
        prompt="Get all GPU  products from this page",
        source=page,
        config=graph_config
    )
  
  result = smart_scraper_graph.run()
  
  arr_all.append(result['GPU_Products'])
  

# write to file
with open('data.json', 'w') as f:
	json.dump(arr_all, f)
