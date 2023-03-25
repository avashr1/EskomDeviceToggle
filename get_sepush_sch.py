import os
import requests
import json

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

SEPUSH_TOKEN = os.environ["SEPUSH_TOKEN"]
SEPUSH_AREA_ID = os.environ["SEPUSH_AREA_ID"]

url = "https://developer.sepush.co.za/business/2.0/status"

payload = {}
headers = {'token': SEPUSH_TOKEN}

response = requests.request("GET", url, headers=headers, data=payload)

data = json.loads(response.text)
s = data
stage_current = s['status']['eskom']['stage']
stage_current_time = s['status']['eskom']['stage_updated']

fs = open('Stage.txt', 'r')
stage_prev = fs.readline()
stage_prev_time = fs.readline()
fs.close()
if stage_current != stage_prev and stage_current_time != stage_prev_time:
    fs1 = open('Stage.txt', 'w')
    fs1.write(stage_current)
    fs1.write("\n")
    fs1.write(stage_current_time)
    fs1.close()

    url = "https://developer.sepush.co.za/business/2.0/area?id=" + SEPUSH_AREA_ID

    payload = {}
    headers = {'token': SEPUSH_TOKEN}

    response = requests.request("GET", url, headers=headers, data=payload)

    f = open('json_data.json', 'w')
    f.write(response.text)
    f.close()
# ---------
