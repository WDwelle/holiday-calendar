import urllib.request, urllib.error, urllib.parse
import json



url = "https://holidayapi.com/v1/holidays" 
params = { 
    "key": "a1b7e2c8-f428-4065-8758-3bfb689c3448", #API key
    "year": "2020", 
    "country": "US",
    "month": "12",
    "day" : "31"
}    

query_string = urllib.parse.urlencode( params ) 

url = url + "?" + query_string 

with urllib.request.urlopen( url ) as response: 
    response_text = response.read() 
    #print( response_text ) 


day = json.loads( response_text )
holiday = (day['holidays'])
print (holiday[0].get('name'), holiday[0].get('weekday').get('date').get('name'))