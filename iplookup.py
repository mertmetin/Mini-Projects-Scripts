import requests, json
import urllib2


#Gets your ip address automatically
def get_ip_address():
    my_ip = urllib2.urlopen('http://ip.42.pl/raw').read()
    
    return my_ip

#Parses json data
def parse(ip_address):
    
    #open and read data
    fetch = requests.get("http://freegeoip.net/json/" + ip_address)
    
   
    #parse json data
    data = json.loads(fetch.content)
    
    
    country_name = data["country_name"]
    region_name = data["region_name"]   
    city = data["city"]
        
    return city, region_name, country_name
    
def main():
    print "Getting your ip address and geolocation"
    my_ip = get_ip_address()
    city, region_name, country_name = parse(my_ip)
    print city, region_name, country_name, my_ip
    
if __name__ == "__main__":
    main()
