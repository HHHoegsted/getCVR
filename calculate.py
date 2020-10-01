import json
from collections import Counter
from pprint import pprint as pp

#load json object from file
with open('company_info.json', 'r') as f:
	data = json.load(f)

#generate counter for each industry type in json objects
result = Counter(company['industry'] for company in data)
#convert to dictionary
result = dict(result)
#print it nicely
pp(result)