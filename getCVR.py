import requests
import json
import csv
import time

#you need this if you want more than 50ish calls to the api
apikey = ''

# initialize empty array of urls to call the api with
urls = []

#have a file with cvr numbers separated by a comma
with open('cvrnumre.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		#generate a url for each cvr
		string = 'http://' + apikey + 'cvrapi.dk/v1/dk/company/' + str(row[0])
		#append url to list of urls	 
		urls.append(string)	

#initialize empty result array and start counter
results = []	
i = 1
#get start time
t1 = time.perf_counter()

#headers required by cvrapi.dk - edit with your own info
headers = {'user-agent': 'company - project - email to project owner' }

for url in urls:
	#get data from each url in turn
	r = requests.get(url)	

	#if the company exists (some test-companies with fake cvrs were in my data)
	if r.status_code == 200:
		#json encode the response
		company = r.json()

		#put the data in variables
		cvr = company['vat']
		name = company['life']['name']
		industry = company['industrycode']['text']
		code = company['industrycode']['code']

		#construct data object with the desired data
		data = {
			'cvr': cvr,
			'industrycode': code,
			'industry': industry,
			'companyname' : name
		}

		#append the data to results array
		results.append(data)
		#wait so we dont overload the server - wait for the same time as the request took
		time.sleep(r.elapsed.total_seconds())

		#display elapsed time per company
		print(f'{i}: Got {name} in {r.elapsed.total_seconds()} seconds')
		i += 1

#get end time
t2 = time.perf_counter()

#write results to json object in file
with open('company_info_with_cvr.json', 'w') as f:
	json.dump(results, f, indent=2)

#display total elapsed time
print(f'Finished in {t2-t1} seconds')
