import pytest
from api.adapters.fish_adapter import FishAdapter
from api.lib.db import drop_records, test_conn, test_cursor
from api.models import Fish
import decimal


response_fish={"year":"2022","county":"Essex","waterbody":"Stevens Pond","town":"Wilmington",
               "month":"May","number":"200","species":"Brown Trout","size_inches":"12"}

@pytest.fixture()
def clean_tables():
    drop_records(test_cursor, test_conn, "ny_fishes")

    yield
    drop_records(test_cursor, test_conn, "ny_fishes")


def test_initializes_with_response_fish():
    fish_adapter_obj=FishAdapter(response_fish)
    assert isinstance(fish_adapter_obj.response_fish, dict)==True

def test_response_fish_does_not_change_when_stored_as_instance():
    fish_adapter_obj=FishAdapter(response_fish)
    assert fish_adapter_obj.response_fish==response_fish

def test_select_attributes():
    fish_adapter_obj=FishAdapter(response_fish)
    fish_attrs=fish_adapter_obj.select_attributes()
    assert fish_attrs=={"waterbody":"Stevens Pond", "species":"Brown Trout",
                        "size_inches":"12", "number":"200", "month":"May",
                        "year":"2022"}

def test_returns_a_fish(clean_tables):
    adapter=FishAdapter(response_fish)
    fish=adapter.run(test_conn, test_cursor)
    assert isinstance(fish, Fish)==True

def test_extracts_waterbody_species_size_inches_number_month_year(clean_tables):
    adapter=FishAdapter(response_fish)
    fish=adapter.run(test_conn, test_cursor)
    assert list(fish.__dict__.keys())==["id", "waterbody", "species", "size_inches",
                                        "number", "month", "year"]
    assert list(fish.__dict__.values())[1:]==['Stevens Pond', 'Brown Trout', decimal.Decimal('12'),
                                              200, 'May', 2022]
