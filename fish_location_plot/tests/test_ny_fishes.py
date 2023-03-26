from src.ny_fishes import *

#Show all fish species in the Black River in NY


#fish_1=fishes[0]
#{'location': {'latitude': '44.918344554', 'needs_recoding': False, 'longitude': '-74.293337254'},
# 'point_y': '44.918344554',
# ':@computed_region_yamh_8v7k': '188',
# 'name': 'Trout River',
# 'comments': 'None',
# 'point_x': '-74.293337254',
# ':@computed_region_wbg7_3whc': '218',
# 'fish_spec': 'Brown Trout*',
# ':@computed_region_kjdx_g34t': '621',
# 'spec_regs': {'url': 'http://www.dec.ny.gov/outdoor/31444.html'},
# 'county': 'Franklin'}

def test_import_correctly():
    fishes=get_fish_data()
    fish_1=fishes[0]
    assert fish_1=={'location': {'latitude': '44.918344554', 'needs_recoding': False, 'longitude': '-74.293337254'}, 'point_y': '44.918344554', ':@computed_region_yamh_8v7k': '188', 'name': 'Trout River', 'comments': 'None', 'point_x': '-74.293337254', ':@computed_region_wbg7_3whc': '218', 'fish_spec': 'Brown Trout*', ':@computed_region_kjdx_g34t': '621', 'spec_regs': {'url': 'http://www.dec.ny.gov/outdoor/31444.html'}, 'county': 'Franklin'}

def test_unique_fish_list():
    fishes = get_fish_data()
    unique_species=fish_species(fishes)
    fish=unique_species[0]
    assert fish not in unique_species[1:]

def test_request_by_waterbody():
    black_river=request_by_waterbody("black river")
    first=black_river[0]
    assert first["name"]=="Black River"

def test_fishes_in_black_river():
    fishes=get_fish_data()
    extracted_fishes=extract_details_from_fishes(fishes)
    fishes_black_river=fishes_in_black_river(extracted_fishes)
    assert fishes_black_river[0]["name"]=="Black River"