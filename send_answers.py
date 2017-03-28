import requests
import json

uri = "http://localhost:9200/beeva/oswaldo/2?pretty"
with open('introduction_quiz.json') as data_file:    
	d = json.load(data_file)

response = requests.post(uri, json=d)
results = json.loads(response.text)
print(response.text)
#print(results)
