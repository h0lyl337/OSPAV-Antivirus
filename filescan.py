import __main__
import os
import hashlib
import requests
import json
import getpass
import sqlite3
import threading
import hashdatabase


def checkstartupfolder():
    print('checking start folder')
    for files in os.listdir(
            'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup' % getpass.getuser()):
        if '.exe' in files:
            file = open(
                'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\%s' % getpass.getuser() % files)
            hash = hashlib.md5(file)
            print(hash.hexdigest)


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


def add_clean_hash(hash):
    hash_list = []
    with open('{}\\clean_hash'.format(os.getcwd()), 'a+') as rx:
        for line in rx.readlines():
            hash_list.append(line.rstrip())
        hash_list.append(hash)
        print(hash_list)
        for line in hash_list:
            rx.writelines(line + '\n')


def return_download_hash_list():
    hash_list = []
    with open('{}\\clean_hash'.format(os.getcwd(), 'r')) as rx:
        for line in rx.readlines():
            hash_list.append(line.rstrip())
            rx.close()
        return hash_list


def scan_downloads():
    __main__.update_text('Scanning Downloads')
    for file in os.listdir('C:\\users\\{}\\Downloads'.format(getpass.getuser())):
        __main__.root.update()
        if '.exe' in file:
            __main__.root.update()
            opened_file = open('C:\\users\\{}\\Downloads\\{}'.format(os.getcwd(), file), 'rb')
            readfile = hashlib.md5(opened_file.read())
            hash = readfile.hexdigest()
            if hash not in return_download_hash_list():
                if hashdatabase.find_hash(hash) == hash:
                   print('match found')
                   __main__.update_text('file deleted %s' % file)
                   __main__.root.update()

                else:
                    print('no match')
                    add_clean_hash(hash)
                    __main__.update_text('file %s seem clean' % file)
                    __main__.root.update()
            else:
                pass

    __main__.root.update()