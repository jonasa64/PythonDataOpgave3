import os
import json
import numpy as np
import urllib.request as req

class Json_handler:
    dataset = None
    icd = []
    cause = []
    state = []
    json = ''
    csv = ''

    def generate(self):
        print("Interpretating ...")
        self.dataset = np.genfromtxt(self.csv, delimiter=',', dtype='uint16')
        print("Done")

    def __init__(self, file):
        self.json = file + ".json"
        self.csv = file + ".csv"

        print("Converting JSON-file to CSV ...")

        with open(self.json, encoding="UTF8") as fp:
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
            icd = {key: item for item, key in enumerate(icd, i)}
            i = 1
            cause = {key: item for item, key in enumerate(cause, i)}
            i = 1
            state = {key: item for item, key in enumerate(state, i)}

            if not os.path.isfile(self.csv):

                csv = ''
                for row in data:
                    row[9] = icd[row[9]]
                    row[10] = cause[row[10]]
                    if row[11] != "United States":
                        row[11] = state[row[11]]
                    else:
                        row[11] = 0

                    csv += ','.join(str(item) for item in row[8:])
                    csv += "\n"

                with open(self.csv, "w") as fw:
                    fw.write(csv)
            else:
                print("CSV-file already exists!")
                print("Meta-data for JSON generated.")

            self.icd = ["United States"] + list(icd)
            self.cause = ["None"] + list(cause)
            self.state = ["None"] + list(state)

        print("Done")


def download(url, to=None):
    print("Downloading file ...")
    opener = req.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')]
    req.install_opener(opener)
    req.urlretrieve(url, to)
    print("Done")

    return True


dataset_keys = ["year", "icd", "cause", "state", "deaths", "deaths_age_adj"]
fileurl = "https://data.cdc.gov/api/views/bi63-dtpu/rows.json?accessType=DOWNLOAD"
filename = "NCHS_Leading_Causes_of_Death:_US"


def initialize():
    if not os.path.isfile(filename + ".json"):
        download(fileurl, filename + ".json")

    jhandle = Json_handler(filename)

    jhandle.generate()

    return jhandle

data = initialize()
