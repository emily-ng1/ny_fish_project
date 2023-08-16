import requests

class ClientFish:
    URL="https://data.ny.gov/resource/e52k-ymww.json"

    def request_fishes(self):
        response=requests.get(self.URL)
        return response.json()