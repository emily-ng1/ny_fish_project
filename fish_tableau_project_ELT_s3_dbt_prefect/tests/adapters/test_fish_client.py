from api.adapters.client_fish import ClientFish


def test_fish_url():
    fish_client_obj=ClientFish()
    assert fish_client_obj.URL=="https://data.ny.gov/resource/e52k-ymww.json"

def test_request_fishes():
    fish_client_obj=ClientFish()
    fish_json=fish_client_obj.request_fishes()
    sorted_keys=list(sorted(fish_json[0].keys()))
    assert sorted_keys==sorted(["year", "county", "waterbody", "town", "month","number", "species", "size_inches"])