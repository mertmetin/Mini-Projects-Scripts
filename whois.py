import urllib2
 
def whois(domain):
    api_key  = "ed022ebbdd54d05003bc52832a200779"
    template = "http://api.robowhois.com/whois/%s"
 
    passman   = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, "http://api.robowhois.com/", api_key, "X")
    handler   = urllib2.HTTPBasicAuthHandler(passman)
    opener    = urllib2.build_opener(handler)
    request   = urllib2.Request(template % domain)
    response  = opener.open(request)
 
    return response.read()
 

def main():
    domain = raw_input("Enter the domain you would like to search: \n")
    print whois(domain)
    
    
if __name__ == "__main__":
    main()
