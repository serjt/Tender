import requests
import json

post_url = 'http://213.159.215.186/api/v1/user/'
post_data = {'username': 'username',
             'password': "user1234",
             'email': "tre@m.ru",}
headers = {'Content-type': 'application/json'}

r = requests.post(post_url, json.dumps(post_data), headers=headers)
print r.status_code
