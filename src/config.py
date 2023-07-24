import os

api_secret = os.environ.get("GANDI_API_SECRET", "TOKEN").replace("\"","")
api_endpoint = os.environ.get("GANDI_API_ENDPOINT",'https://dns.api.gandi.net/api/v5').replace("\"","") 

static_ip = os.environ.get("GANDI_STATIC_IP","").replace("\"","") 
domain = os.environ.get("GANDI_DOMAIN","").replace("\"","") 
subdomains = os.environ.get("GANDI_SUBDOMAINS","").replace("\"","").split(",")
ttl = os.environ.get("GANDI_TIMEOUT","300").replace("\"","") 
ifconfig = os.environ.get("GANDI_IFCONFIG","https://ifconfig.co/ip").replace("\"","") 
