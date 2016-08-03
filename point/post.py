import requests
import json

# post_url = 'http://localhost:8000/api/v1/user/'
# post_data = {'username': 'username',
#              'password': "user1234",
#              'email': "tre@m.ru",}
# headers = {'Content-type': 'application/json'}
post_url = 'http://localhost:8000/api/v1/story/'
post_data = {'user':"/api/v1/user/4/",
            'title': "asdfsd",
             'text': "treru",
             'publish':False}
headers = {'Content-type': 'application/json'}
r = requests.post(post_url, json.dumps(post_data), headers=headers)
print r.status_code
