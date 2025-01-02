import os
import json
# from scrapegraphai.graphs import SmartScraperGraph
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperMultiGraph

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

sources = [
    "https://hotgear.vn/products/vga-zotac-gaming-geforce-rtx-4080-super-trinity-black-edition-16gb-gddr6x",
    "https://tinhocngoisao.com/products/card-man-hinh-vga-zotac-gaming-geforce-rtx-4080-super-trinity-black-edition-16gb-gddr6x-zt-d40820d-10p",
    "https://tandoanh.vn/inno3d-geforce-rtx-4080-super-x3-16gb-gddr6x/"
]


# Create the SmartScraperGraph instance
# smart_scraper_graph = SmartScraperGraph(
#     prompt="Extract gpu info and price",
#     source="https://hotgear.vn/products/vga-zotac-gaming-geforce-rtx-4080-super-trinity-black-edition-16gb-gddr6x",
#     config=graph_config
# )

# Run the pipeline
# result = smart_scraper_graph.run()

multiple_search_graph = SmartScraperMultiGraph(
    prompt="Extract gpu name, brand, and price",
    source=sources,
    config=graph_config,
    schema=None,
)
result = multiple_search_graph.run()

print(json.dumps(result, indent=4))