# Only for tests
user = 'newboard'
password = 'newboard'
#
# Init
import http.client
import hashlib
import json
import base64 # base64.b64decode(encoded_string)

header = {'Authorization':'Digest username=%s, realm=%s, nonce=%s, uri=%s, response=%x'}

conn = http.client.HTTPConnection('localhost', 3000);
hasg = hashlib.md5()
#
# Create new board

conn.request('GET', '/newboard')

conn.request('GET', '/newboard')
#
# Read Data
	# Send data to server