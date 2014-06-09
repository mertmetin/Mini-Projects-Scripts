"""
Example usage: python weather.py J9J0E4 for Canada or 32311 for US
"""

import requests, json
from sys import argv

scp, postal_code = argv

#Fetchs the weather information
def parse_weather_json(postal_code):

    #open and read data
    fetch = requests.get("http://api.worldweatheronline.com/free/v1/weather.ashx?key=fe88638486dc6fc5018226fb5147fd4df0746a5d&format=json&" + "q=" +    postal_code)
    
    #parse json data
    data = json.loads(fetch.content)
    
    
    for a in data["data"]["current_condition"]:
        for b in a:
            current_weather = a["temp_C"]
                    
    return current_weather 
    
#Fetchs the location information
def parse_location_json(postal_code):

    #open and read data
    fetch = requests.get("http://api.worldweatheronline.com/free/v1/search.ashx?key=fe88638486dc6fc5018226fb5147fd4df0746a5d&format=json&" + "q=" +    postal_code)
    
    #parse json data
    data = json.loads(fetch.content)
    area_name = []
    country = []
    region = []
    
    for a in data["search_api"]["result"]:
        area_name.append(a["areaName"])
        country.append(a["country"])
        region.append(a["region"])
       
    country[0] = edit_value(country[0])
    region[0] = edit_value(region[0])
    area_name[0] = edit_value(area_name[0])
    
    return country[0], region[0], area_name[0]
    
#Removes the CDATA from the value
def edit_value(val):
    val = str(val)
    
    val = val[14:-3]
    
    return val
    
def main():
    print "Getting your current weather information..."
    weather = parse_weather_json(postal_code)
    country, region, area_name = parse_location_json(postal_code)
    print area_name, region + "," + country , weather + "C"
    
if __name__ == "__main__":
    main()
