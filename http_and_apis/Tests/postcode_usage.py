import requests
from Models.single_postcode_model import SinglePCModel

class SinglePC():

    def __init__(self, postcode):
        self.url = "https://api.postcodes.io/postcodes/" + postcode
        self.request = requests.get(self.url)
        self.headers = self.request.headers
        self.response_json = self.request.json()

    def response(self):
        return SinglePCModel(self.response_json)


pc = SinglePC("B38 8AG")
print(pc.response().latitude)