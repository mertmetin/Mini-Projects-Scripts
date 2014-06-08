"""
Example usage: python weather.py J9J0E9 for Canada
"""

import requests, json
from sys import argv

scp, postal_code = argv

def parse_json(postal_code):

    #open and read data
    fetch = requests.get("http://api.worldweatheronline.com/free/v1/weather.ashx?key=API_KEY_HERE&q=" + postal_code + "&format=json")
    
    #parse json data
    data = json.loads(fetch.content)
    
    for a in data["data"]["current_condition"]:
        for b in a:
            current_weather = a["temp_C"]
    
    return current_weather
    
def main():
    print "Getting your current weather information..."
    weather = parse_json(postal_code)
    print weather
    
if __name__ == "__main__":
    main()
