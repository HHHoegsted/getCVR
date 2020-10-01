# getCVR
Getting information from cvrapi.dk on a lot of companies? 

We have 7.5k clients and someone up the food chain wanted to see which type of companies were most profitable. 
This little project (getCVR.py) takes in a list of 8-digit CVR-numbers (like social security numbers for companies), and first converts them
to a json file with info on CVR, company name, industry code and industry description.

the second part (calculate.py) finds out how many companies of each type are in the list, and outputs that.

I took the json-file generated from the first script and ran a php script against our database, generating a list of how many cases we had overall and average 
per company type.
