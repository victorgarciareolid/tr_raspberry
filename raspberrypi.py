from requests.auth import HTTPDigestAuth
import requests
import json

addr = "http://localhost:3000"
username = "holamundo"
password = "contrasenya"

header = {"Content-type":"application/json", "Accept":"text/plain"}
sample = {"concentration":2.22}

params = json.dumps(sample, sort_keys=True)

request = requests.post(addr,auth=HTTPDigestAuth(username, password), data=params, headers=header)


