import pytest
from api.models import Fish
from api.lib.db import drop_all_tables, test_conn, test_cursor, save


@pytest.fixture()
def fish():
    drop_all_tables(test_conn, test_cursor)

    yield
    drop_all_tables(test_conn, test_cursor)


def test_fish_mass_assignment():
    fish=Fish(year=2021, county="Warren", waterbody="Accessible Pond 1", town="Hatchery", 
              month="April", number=30, species="Rainbow Trout", size_inches=9.5)
    assert fish.__dict__=={"year":2021, "county":"Warren", "waterbody":"Accessible Pond 1", "town":"Hatchery", 
                           "month":"April", "number":30, "species":"Rainbow Trout", "size_inches":9.5}

def test_save_fish():
    fish=Fish(year=2021, county="Warren", waterbody="Accessible Pond 1", town="Hatchery", 
              month="April", number=30, species="Rainbow Trout", size_inches=9.5)
    saved_fish=save(fish, test_conn, test_cursor)
    
    assert type(saved_fish.id)==int
    assert saved_fish.species=="Rainbow Trout"