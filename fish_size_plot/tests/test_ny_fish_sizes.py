from src.ny_fish_sizes import *


first_fish_size={'year': '2021',
                 'county': 'Warren',
                 'waterbody': 'Accessible Pond 1',
                 'town': 'Hatchery',
                 'month': 'April',
                 'number': '30',
                 'species': 'Rainbow Trout',
                 'size_inches': '9.5'}


def test_import_correctly():
    fishes=get_fish_size_data()
    fish_1=fishes[0]
    assert fish_1==first_fish_size

def test_unique_fish_list():
    fishes_size=get_fish_size_data()
    unique_species=unique_fish_size_species(fishes_size)
    fish=unique_species[0]
    assert fish not in unique_species[1:]

def test_calc_fish_avg_size():
    fishes_size = get_fish_size_data()
    unique_fish = unique_fish_size_species(fishes_size)
    fish_avg_size_inches = calc_fish_avg_size(unique_fish, fishes_size)

    assert max(fish_avg_size_inches, key=lambda x:x["avg_size_inches"])["species"]=='Brown Trout'



