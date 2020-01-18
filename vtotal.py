import requests
import json
import __main__
from tkinter import *


def VirusTotalScan32up(file):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': 'keyhere'}
    files = {'file': (file, open(file, 'rb'))}
    response = requests.post(url, files=files, params=params)
    jsondata = json.loads(response.text)
    print(jsondata)


def get_hash_report(hash, file):
    try:
        url = 'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey': 'keyhere', 'resource': '%s' % hash}
        response = requests.get(url, params=params)
        jsondata = json.loads(response.text)
        detected = jsondata['positives']
        totalscans = jsondata['total']
        print(str(detected) + '/' + str(totalscans))
        return detected
    except:
        pass


def enable_vtotal():
    if __main__.check_auto_vtotal() == TRUE:
        print('Virus-Total is enabled')
        __main__.checkbox_auto_vtotal.config(fg="green")
        __main__.root.update()
