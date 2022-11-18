import sys
import requests
url=sys.argv[1]
try :
    response=requests.get(url)
    print("HTTP Response code:",response.status_code)
except:
    print("error, wrong url, or no connection")