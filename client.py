from requests.auth import HTTPDigestAuth
import requests
import json

header = {'Authorization':'Digest username=%s, realm=%s, nonce=%s, uri=%s, response=%x'}
parameter = {'board':'board34', 'sensor1': 2423, 'sensor2': 141241, 'sensor3': 123 }

parameters = json.dumps(parameter, sort_keys=True)
url = 'http://localhost:3000/newboard'
#r = requests.get(url, auth=HTTPDigestAuth('newboard', 'newboard'))
#print(r.json())
r1 = requests.post('http://localhost:3000/', auth=HTTPDigestAuth('board34', 'board34julian'), data=parameters)
