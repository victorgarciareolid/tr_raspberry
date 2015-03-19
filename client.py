from requests.auth import HTTPDigestAuth
import requests
import hashlib
import json
import base64

header = {'Authorization':'Digest username=%s, realm=%s, nonce=%s, uri=%s, response=%x'}

url = 'http://localhost:3000/newboard'

r = requests.get(url, auth=HTTPDigestAuth('newboard', 'newboard'))
print(r.json())