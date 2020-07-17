import json
import requests
from pprint import pprint

class httpPractise:

    def __init__(self):
        self.postcode = 'B38 8AG'
        self.dict_body = {'postcodes': [self.postcode]}
        self.json_body = json.dumps(self.dict_body)
        self.headers = {'Content-Type': 'application/json'}
        self.address = "http://api.postcodes.io/postcodes/"
        self.req_response = requests.post(self.address, headers=self.headers, data=self.json_body)

    def status(self):
        return self.req_response.json()['status']

    def find_address(self):
        result = req_response.json()["result"]
        return self.req_response.json()


my_postcode = httpPractise()

