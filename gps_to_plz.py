from urlparse import urljoin
import requests
import csv
import re

data =[ ['19552', '-10.9442376856709', '-37.0879052749376', '38082', '2015-11-23 22:24:25'],
['19553', '-10.9441598691513', '-37.0887022464116', '38082', '2015-11-23 22:24:32'],
['19554', '-10.9439778683169', '-37.0894213230478', '38082', '2015-11-23 22:24:42'],
#['19556', '-10.9434686302044', '-37.0890712840714', '38082', '2015-11-23 22:24:57'],
#['19557', '-10.9434686302044', '-37.0890712840714', '38082', '2015-11-23 22:25:04'],
#['19558', '-10.9335228242084', '-37.078922706708', '38084', '2015-12-16 21:43:16'],
#['19559', '-10.9333981562022', '-37.0788730972165', '38084', '2015-12-16 21:43:28'],
#['19560', '-10.9333981562022', '-37.0788730972165', '38084', '2015-12-16 21:43:39'],
#['19561', '-10.9333981562022', '-37.0788730972165', '38084', '2015-12-16 21:43:50'],
#['19563', '-10.8694503931813', '-37.0952764284214', '38090', '2016-01-03 00:58:12'],
#['19564', '-10.8694503931813', '-37.0952764284214', '38090', '2016-01-03 00:58:23'],
#['19565', '-10.92372234', '-37.10657943', '38092', '2016-01-19 13:01:01'],
#['19566', '-10.92370353', '-37.1066926', '38092', '2016-01-19 13:01:12'],
#['19567', '-10.92371484', '-37.10668794', '38092', '2016-01-19 13:01:24'],
#['19568', '-10.92371522', '-37.10668813', '38092', '2016-01-19 13:01:36'],
#['19569', '-10.92371551', '-37.10668792', '38092', '2016-01-19 13:01:47'],
]


#functional programming
#print range(len(data))
lats = map(float,map(lambda x:data[x][1],range(len(data))))
lngs = map(float,map(lambda x:data[x][2],range(len(data))))
#print lat
#print lng
gps = zip(lats,lngs)
print gps

url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key=AIzaSyCNA7_Lq8TJ1lggfLB2kxQFC92B_rRpREg"
t = 0
while t < len(gps):
	print "send:" + url.format(lat=gps[t][0],lng=gps[t][1]) 
	response = requests.get(url.format(lat=gps[t][0],lng=gps[t][1]))
	#processed_text = response.text.split()
	f = open("gps_data.txt","wb")
	f.write(response.text)
	#find the index of the postal code,so we can go back to the PLZ
	#the ori_index is 119. the PLZ is 115
	#for text in processed_text:
	#	if text == '"postal_code"':
	#		ori_index = processed_text.index(text)
	#		print ori_index
	
	#print processed_text[115]
	
	#[0]["address_components"][7]["long_name"]
	t += 1
f.close()