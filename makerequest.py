import requests
def makerequest(id):
    r = requests.get(url = "http://10.56.9.186:8000/kiosk/login", params = {"id":str(id), "kiosk":str("2")})
    print("finished")
    rdata = r.json()
    print(rdata)