import requests
import json


#assigning a variable for the link we have assigned on our cluster
url="http://35.229.83.99/nxchallenge/astarisborn"

#Send a GET request to the server
r = requests.get(url)

##load the data into the variable by jsonifying it
t = json.loads(r.content) 

#For loop to print every associated data
for i in range(len(t)):
    print(t[i])