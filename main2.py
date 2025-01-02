# https://hotgear.vn/collections/vga-card-man-hinh

import os
import json

import requests

from scrapegraphai.graphs import SmartScraperGraph
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


page_pattern = "https://hotgear.vn/collections/vga-card-man-hinh?q=filter=((collectionid:product=1001473971))&page="

list_pages = [page_pattern + str(i) for i in range(1, 2)]




# # Run the graph
# results = graph.run()

# # Use Ollama for additional processing
# def ollama_query(prompt):
#     response = requests.post(
#         "https://api.ollama.ai/v1/query",
#         json={"prompt": prompt},
#         headers={"Authorization": "Bearer YOUR_OLLAMA_API_KEY"}
#     )
#     return response.json()

# # Example: Analyze scraped data
# for result in results["parse_gpu"]:
#     prompt = f"Summarize and categorize this GPU: {result['name']}"
#     response = ollama_query(prompt)
#     print("Ollama response:", response["output"])


# # Define the configuration for the scraping pipeline
graph_config = {
    # "llm": {
    #     "api_key": api_key,
    #     "model": "openai/gpt-4o-mini",
    # },
    # "verbose": True,
    # "headless": False,
    "llm": {
        "model": "ollama/mistral",
        "temperature": 0,
        "format": "json",  # Ollama needs the format to be specified explicitly
        "base_url": "http://localhost:11434",  # set Ollama URL
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "base_url": "http://localhost:11434",  # set Ollama URL
    }
}

# page_pattern = "https://hotgear.vn/collections/vga-card-man-hinh?q=filter=((collectionid:product=1001473971))&page="

# list_pages = [page_pattern + str(i) for i in range(1, 56)]

# print(list_pages)

arr_all = []

for page in list_pages:
	
  smart_scraper_graph = SmartScraperGraph(
        prompt="Get all GPU  products from this page",
        source=page,
        config=graph_config
    )
  
  result = smart_scraper_graph.run()
  
  arr_all.append(result)
  

# write to file
with open('data2.json', 'w') as f:
	json.dump(arr_all, f)
