import requests

class ClientWaterQuality:
    URL="https://data.ny.gov/resource/8xz8-5u5u.json"

    def request_water_qualities(self):
        response=requests.get(self.URL)
        return response.json()