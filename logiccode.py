import requests
import csv
def getids():
    ids={}
    with open('ids.csv', mode='r') as f:
        reader=csv.reader(f)
        x = 0
        for row in reader:
            name, id = row[1], row[0]
            x = x + 1
            if x == 1: continue
            separated_name = name.lower().split(",")
            first = separated_name[1]
            last = separated_name[0]
            combined = first + "_" + last
            ids[combined[1:]] = id
    return ids
def makerequest(id):
    r = requests.get(url = "http://10.56.9.186:8000/kiosk/login", params = {"id":str(id), "kiosk":str("2")})
    print("finished")
    rdata = r.json()
    return rdata