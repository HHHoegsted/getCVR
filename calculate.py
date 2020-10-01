import json
from collections import Counter
from pprint import pprint as pp

with open('company_info.json', 'r') as f:
	data = json.load(f)							#load json object from file

result = Counter(company['industry'] for company in data)	#generate counter for each industry type in json objects
result = dict(result)		#convert to dict
pp(result)					#print it nicely