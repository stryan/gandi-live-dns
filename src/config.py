import os

api_secret = os.environ.get("GANDI_API_SECRET", "TOKEN")
api_endpoint = os.environ.get("GANDI_API_ENDPOINT",'https://dns.api.gandi.net/api/v5')

static_ip = os.environ.get("GANDI_STATIC_IP","")
domain = os.environ.get("GANDI_DOMAIN","")
subdomains = os.environ.get("GANDI_SUBDOMAINS","").split(",")
ttl = os.environ.get("GANDI_TIMEOUT","300")
ifconfig = os.environ.get("GANDI_IFCONFIG","https://ifconfig.co/ip")
