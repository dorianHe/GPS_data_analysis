import json as js

with open("gps_data.py","r") as f:
	data = js.load(f)

i = 0
while i < len(data['results']):
	for element in data['results'][i]['address_components'][0]['types']:
		if element == 'postal_code':
			print i,data['results'][i]['address_components'][0]['long_name']
	i+= 1