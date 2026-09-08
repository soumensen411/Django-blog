import requests
import json

URL = "http://127.0.0.1:8000/creatstudent/"

data = {
    'name': 'Nasimul Islam',
    'roll':45,
    'section':'6DM'
}
json_data = json.dumps(data)

r = requests.post(url= URL, data = json_data)

res_data = r.json()
print(res_data)