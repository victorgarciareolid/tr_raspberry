from requests.auth import HTTPDigestAuth
import requests
import json

header= {'Content-type': 'application/json', 'Accept': 'text/plain'}
parameter = {'board':'board1', 'sensor1': 2423, 'location': {'lat': 40, 'lon': 21.23}};

parameters = json.dumps(parameter, sort_keys=True)
 
#url = 'http://localhost:3000/newboard'
#r = requests.get(url, auth=HTTPDigestAuth('newboard', 'newboard'))
#print(r.json())
r1 = requests.post('http://localhost:3000/', auth=HTTPDigestAuth('board1', 'board1julian'), data=parameters, headers=header)
