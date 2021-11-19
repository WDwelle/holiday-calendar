from flask_app import app
from flask import render_template,redirect,request,session,flash
import urllib.request, urllib.error, urllib.parse
import json

#GET
@app.route("/")
def index():
    return render_template("index.html")


#POST
@app.route("/pick_date", methods = ["POST"])
def process():
    data ={
        "new_date" : request.form.get("myDate")
    }
    myDay = data["new_date"]
    newDay = myDay.split("-")
    day = newDay[2]
    month = newDay[1]
    year = 2020
    print(day)
    print(month)
    #api call
    url = "https://holidayapi.com/v1/holidays" 
    params = { 
        "key": "a1b7e2c8-f428-4065-8758-3bfb689c3448", #API key
        "year": "2020", 
        "country": "US",
        "month": month,
        "day" : day
    }

    query_string = urllib.parse.urlencode( params ) 

    url = url + "?" + query_string 

    with urllib.request.urlopen( url ) as response: 
        response_text = response.read() 
        #print( response_text ) 

    holiday = ''
    day = json.loads( response_text )
    holiday = (day['holidays'])
    print(holiday)
    if (holiday):
        return render_template("info.html", all_holidays = holiday, todaysDate = myDay)
    else:
        #flash ("No Holidays!")
        return redirect("/")