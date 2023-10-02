import pytest
from api.models import Fish
from api.lib.db import drop_all_tables, test_conn, test_cursor, save, find_all


@pytest.fixture()
def clean_tables():
    drop_all_tables(test_conn, test_cursor)

    yield
    drop_all_tables(test_conn, test_cursor)


def test_fish_mass_assignment():
    fish=Fish(year=2021, waterbody="Accessible Pond 1",
              month="April", number=30, species="Rainbow Trout", size_inches=9.5)
    assert fish.__dict__=={"year":2021, "waterbody":"Accessible Pond 1",
                           "month":"April", "number":30, "species":"Rainbow Trout", "size_inches":9.5}

def test_save_fish(clean_tables):
    fish=Fish(year=2021, waterbody="Accessible Pond 1",
              month="April", number=30, species="Rainbow Trout", size_inches=9.5)
    saved_fish=save(fish, test_conn, test_cursor)

    assert type(saved_fish.id)==int
    assert saved_fish.species=="Rainbow Trout"

def test_duplicate_fish(clean_tables):
    fish=Fish(year=2021, waterbody="Accessible Pond 1",
              month="April", number=30, species="Rainbow Trout", size_inches=9.5)
    saved_fish=save(fish, test_conn, test_cursor)

    fish=Fish(year=2021, waterbody="Accessible Pond 1",
              month="April", number=30, species="Rainbow Trout", size_inches=9.5)
    saved_fish=save(fish, test_conn, test_cursor)

    fishes=find_all(Fish, test_conn)
    assert [fish.species for fish in fishes]==["Rainbow Trout"]



@pytest.fixture()
def save_fishes():
    drop_all_tables(test_conn, test_cursor)

    fish_1=Fish(**{"year": "2022", "waterbody": "South Sandy Creek", "month": "May",
            "number": "590", "species": "Brook Trout", "size_inches": "9"})
    saved_fish_1=save(fish_1, test_conn, test_cursor)

    fish_2=Fish(**{"year":"2022", "waterbody":"Sawkill Creek", "month":"April",
                   "number":"930","species":"Brown Trout","size_inches":"9"})
    saved_fish_2=save(fish_2, test_conn, test_cursor)

    yield
    drop_all_tables(test_conn, test_cursor)


def test_find_all_species(save_fishes):
    fishes=find_all(Fish, test_conn)
    assert [fish.species for fish in fishes]==["Brook Trout", "Brown Trout"]


