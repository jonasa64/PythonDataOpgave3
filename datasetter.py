import os
import json
import numpy as np
import urllib.request as req

# create Json_handler class to convert the .json file to csv, and contain indexing keys(icd, cause, state) for future use
class Json_handler:
    dataset = None
    icd = []
    cause = []
    state = []
    json = ''
    csv = ''

    # method to generate the dataset for future data-extraction
    def generate(self):
        print("Interpretating ...")
        self.dataset = np.genfromtxt(self.csv, delimiter=',', dtype='uint16')
        print("Done")
        

    # initialize the class, converting the json-file and creating the index-keys(icd, cause, state)
    def __init__(self, file):
        # set the filenames
        self.json = file + ".json"
        self.csv = file + ".csv"

        print("Converting JSON-file to CSV ...")
        
        # open the json file and iterate over the its lines to clean it up a bit

        with open(self.json, encoding="UTF8") as fp:
            json_str = ''
            for line in fp:
                json_str += line
             # retrieve only the "data"-part of the json, excluding meta-data
            data = json.loads(json_str)
            data = data["data"]

            icd = set()
            cause = set()
            state = set()
            
            # iterate through the datarows, to get a set of states, causes and icd-codes used
            for row in data:
                icd.add(row[9])
                cause.add(row[10])
                if row[11] != "United States": # Make sure that "United States" which is not a state is excluded
                    state.add(row[11])

            # sort the sets alfabetically
            icd = sorted(icd)
            cause = sorted(cause)
            state = sorted(state)

            # convert the sets to a list, with indexes corresponding to the sorted sets
            i = 1
            icd = {key: item for item, key in enumerate(icd, i)}
            i = 1
            cause = {key: item for item, key in enumerate(cause, i)}
            i = 1
            state = {key: item for item, key in enumerate(state, i)}

            # if the csv-files has not previously been writen, write it
            if not os.path.isfile(self.csv):

                csv = ''
                #itterate through the data to generate a csv file, making all items comma separated, and adding newline after each row
                for row in data: 
                    row[9] = icd[row[9]]
                    row[10] = cause[row[10]]
                    if row[11] != "United States":
                        row[11] = state[row[11]]
                    else:
                        row[11] = 0

                    csv += ','.join(str(item) for item in row[8:])
                    csv += "\n"
                    
                # open/create and write the csv-file

                with open(self.csv, "w") as fw: 
                    fw.write(csv)
            else:
                print("CSV-file already exists!")
                print("Meta-data for JSON generated.")
            
            # Create zero-indexes for the data-index-lists
            self.icd = ["None"] + list(icd)
            self.cause = ["None"] + list(cause)
            self.state = ["United States"] + list(state)

        print("Done")


# function to download a given url
def download(url, to=None):
    print("Downloading file ...")
    opener = req.build_opener()
    # add headers imitating a browser to enforce download permission from all websites
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')]
    req.install_opener(opener)
    req.urlretrieve(url, to)
    print("Done")

    return True


dataset_keys = ["year", "icd", "cause", "state", "deaths", "deaths_age_adj"] #dataset_keys array to use for future data-indexing
fileurl = "https://data.cdc.gov/api/views/bi63-dtpu/rows.json?accessType=DOWNLOAD" #url to the dataset used
filename = "NCHS_Leading_Causes_of_Death:_US" #local filename

# initialize function downloads and returns the Json_handler-class to be used for data-analysis
def initialize():
    if not os.path.isfile(filename + ".json"): #if the json file doesn't exist, download it
        download(fileurl, filename + ".json")

    jhandle = Json_handler(filename) # initialize the Json_handler class

    jhandle.generate() # generate the dataset

    return jhandle # return the class

data = initialize() # set data as the initialized Json_handler class
