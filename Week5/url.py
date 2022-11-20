import sys
import requests
url=sys.argv[1]
try :
    response=requests.get(url)
    if(response.status_code==200):
        print("There is a working website at this url")
    else:
        print("Website is down")
except:
    print("error, wrong url, or no connection")