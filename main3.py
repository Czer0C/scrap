import os
import json
import re

def extract_gpu_models(strings):
  
	
 pattern = r"(RTX\s\d{4}(?:\s(?:SUPER|Ti|Ti SUPER))?)"
 
 arr = re.findall(pattern, strings)
 
 final_str = " ".join(arr)
 
 return final_str

# read file json
with open('data.json', 'r') as f:
	data = json.load(f)

# flat array
flat_list = [item for sublist in data for item in sublist]

deString = []

for i in flat_list:
  
	if (type(i) == dict):
		discounted_price = i.get("discounted_price")
  
		if discounted_price == None:
			discounted_price = type(i) == dict and i.get("price") or None
			
		obj = {}
	
		f_name = type(i) == dict and i.get("name") or i

		obj["name"] = extract_gpu_models(f_name)
		
		obj["price"] = i.get("price")
		
		obj["link"] = i.get("link")
		
		obj["discounted_price"] = discounted_price

		print(obj)

      
print(deString)