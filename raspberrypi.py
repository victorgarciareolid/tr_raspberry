from requests.auth import HTTPDigestAuth
import requests
import json

txt = open("credentials.txt")

username= txt.readline()
password = txt.readline()

addr = "http://localhost:3000"
header = {"Content-type":"application/json", "Accept":"text/plain"}

def VoltsToPpm():
    pass

def SendEveryNSeconds():
    concentration = VoltsToPpm(MakeMeasurement())
    measurement = {"concentration":concentration}
    JsonData = json.dumps(measurement, sort_keys=True)
    Request = requests.post(addr,auth=HTTPDigestAuth(username, password), data=JsonData, headers=header)

def MakeMeasurement():
    pass
