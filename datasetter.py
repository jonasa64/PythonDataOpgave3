import os
import json
import numpy as np
import urllib.request as req
from urllib.parse import urlparse

def json_to_csv(json_file,csv_file):
    with open(json_file, encoding="UTF8") as fp:
        json_str = ''
        for line in fp:
            json_str += line
        data = json.loads(json_str)
        data = data["data"]
        
        icd = set()
        cause = set()
        state = set()
        
        for row in data:
            icd.add(row[9])
            cause.add(row[10])
            state.add(row[11])
        
        icd = sorted(icd)
        cause = sorted(cause)
        state = sorted(state)
        
        i = 1
        icd = {key:item for item,key in enumerate(icd,i)}
        i = 1
        cause = {key:item for item,key in enumerate(cause,i)}
        i = 1
        state = {key:item for item,key in enumerate(state,i)}
        
        csv = ''
        for row in data:
            row[9] = icd[row[9]]
            row[10] = cause[row[10]]
            row[11] = state[row[11]]

            csv += ','.join(str(item) for item in row[8:])
            csv += "\n"
        
        with open(csv_file, "w") as fw:
            fw.write(csv)
        
        return data
    
def download(url,to=None):
    opener = req.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')]
    req.install_opener(opener)
    req.urlretrieve(url, to)
    
    return True

dataset_keys = ["year","icd","cause","state","deaths","deaths_age_adj"]
fileurl = "https://data.cdc.gov/api/views/bi63-dtpu/rows.json?accessType=DOWNLOAD"
filename = "NCHS_Leading_Causes_of_Death:_US"

def initialize():
    if not os.path.isfile(filename + ".json"):
        print("Downloading file ...")
        download(fileurl,filename + ".json")
        print("Done")
    
    if not os.path.isfile(filename + ".csv"):
        print("Converting JSON-file to CSV ...")
        json_to_csv(filename + ".json", filename + ".csv")
        print("Done")

    print("Interpretating ...")
    data = np.genfromtxt(filename + ".csv", delimiter=',', dtype='uint16')
    print("Done")        
        
    return data

dataset = initialize()
