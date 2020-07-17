import requests
from pprint import pprint
import json

dict_body = {'postcodes': ["B38 8AG"]} #, "OX49 5NU", "M32 0JG", "NE30 1DP"]}
json_body = json.dumps(dict_body)
headers = {'Content-Type': 'application/json'}

address = "http://api.postcodes.io/postcodes/"
req_response = requests.post(address, headers=headers, data=json_body)

print(req_response.json()['status'])

result = req_response.json()["result"]

for postcode in result:
    result = postcode['result']
    print(result['postcode'])


# print(type(req_response))
# #
# # print(req_response.headers)
# # pprint(req_response.json())
#
# result = req_response.json()["result"]
# print(f"Eastings: {result['eastings']}; Northings: {result['northings']}")
# print(f"Nuts code: {result['codes']['nuts']}")