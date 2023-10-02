from api.adapters.client_waterquality import ClientWaterQuality


def test_waterquality_url():
    waterquality_obj=ClientWaterQuality()
    assert waterquality_obj.URL=="https://data.ny.gov/resource/8xz8-5u5u.json"

def test_request_waterquality():
    waterquality_obj=ClientWaterQuality()
    waterquality_json=waterquality_obj.request_water_qualities()
    waterquality_keys=list(sorted(waterquality_json[0].keys()))
    assert waterquality_keys==sorted(["waterbody_class", "segment_id", "win", "name", "description",
                                      "basin", "part", "water_quality_class"])