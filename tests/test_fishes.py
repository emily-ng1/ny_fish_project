from src.fishes import *


info_result={'current_u': {'units': 'm/s', 'value': -0.36524099111557007},
             'current_v': {'units': 'm/s', 'value': -0.20965959131717682},
             'point': {'depth': 30.0, 'latitude': -34.04350160431565, 'longitude': 151.97729673977028, 'on_land': False},
             'salinity': {'units': 'g/kg', 'value': 35.43275451660156},
             'temperature': {'units': 'deg C', 'value': 24.843658447265625}}

def test_location_infos_returns_ocean_info():
    location_depth=location_infos(-34, 152, 30)
    assert location_depth==info_result