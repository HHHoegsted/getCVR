import requests
import json
import csv
import time

apikey = ''		#you need this if you want more than 50ish calls to the api

urls = []	# initialize empty array of urls to call the api with

with open('cvrnumre.csv', newline='') as csvfile:		#have a file with cvr numbers separated by a comma
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		string = 'http://' + apikey +'cvrapi.dk/v1/dk/company/' + str(row[0])	#generate a url for each cvr 
		urls.append(string)			#append url to list of urls

results = []		#initialize empty result array and start counter
i = 1
t1 = time.perf_counter()	#get start time

headers = {'user-agent': 'company - project - email to project owner' } 	#headers required by cvrapi.dk

for url in urls:
	r = requests.get(url)			#get data from each url in turn

	if r.status_code == 200:		#if the company exists (some test-companies with fake cvrs were in my data)
		company = r.json()			#json encode the response

		cvr = company['vat']		#put the data in variables
		name = company['life']['name']
		industry = company['industrycode']['text']
		code = company['industrycode']['code']

		data = {					#construct data object with the desired data
			'cvr': cvr,
			'industrycode': code,
			'industry': industry,
			'companyname' : name
		}

		results.append(data)	#append the data to results array
		time.sleep(r.elapsed.total_seconds())	#wait so we dont overload the server

		print(f'{i}: Got {name} in {r.elapsed.total_seconds()} seconds')	#display elapsed time per company
		i += 1		

t2 = time.perf_counter()		#get end time

with open('company_info_with_cvr.json', 'w') as f:
	json.dump(results, f, indent=2)					#write results to json object in file

print(f'Finished in {t2-t1} seconds')	#display total elapsed time
