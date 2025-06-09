import re
import requests
from datetime import datetime

def isvalid(s):
    pattern=r'^https?://[^\s]+$'
    return re.match(pattern,s) is not None

def urlrequest(url):
    try:
        response=requests.get(url,timeout=5)
        return response.status_code
    except requests.RequestException:
        return None
def log_response(url,status):
    with open("log.txt",'a') as f:
        f.write(f'\n {datetime.now()}->{url}-> {status}-> ')

def file_url():
    with open("url.txt",'r') as f:
        urls=f.read().splitlines()
        for url in urls:
            if isvalid(url):
                status = urlrequest(url)
                log_response(url, status or "not reachable")
            else:
                log_response(url, "invalid format")
    