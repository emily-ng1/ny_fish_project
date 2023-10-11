import pytest
from api.lib.db import drop_records, test_conn, test_cursor
from api.adapters.waterquality_adapter import WaterQualityAdapter
from api.models.water_quality import WaterQuality


response={"waterbody_class":"Estuary","segment_id":"1701-0022","win":"(MW1.3)  UB",
          "name":"Upper New York Bay","description":"entire bay, as described below",
          "basin":"Atlantic Ocean/Long Island Soun","part":"890","water_quality_class":"I"}

@pytest.fixture()
def clean_tables():
    drop_records(test_cursor, test_conn, "ny_water_qualities")

    yield
    drop_records(test_cursor, test_conn, "ny_water_qualities")

def test_initializes_with_response_waterquality():
    waterquality_obj=WaterQualityAdapter(response)
    assert isinstance(waterquality_obj.response_waterquality, dict)==True

def test_response_waterquality_does_not_change_when_stored_as_instance():
    waterquality_obj = WaterQualityAdapter(response)
    assert waterquality_obj.response_waterquality==response

def test_select_attributes():
    waterquality_obj=WaterQualityAdapter(response)
    assert waterquality_obj.selected_attributes()=={"name":"Upper New York Bay",
                                                  "basin":"Atlantic Ocean/Long Island Soun",
                                                  "description":"entire bay, as described below",
                                                  "water_quality_class":"I", "waterbody_class":"Estuary"}
def test_returns_a_fish(clean_tables):
    waterquality_obj = WaterQualityAdapter(response)
    waterquality=waterquality_obj.run(test_conn, test_cursor)
    assert isinstance(waterquality, WaterQuality)==True

def test_extracts_name_basin_description_water_quality_class_waterbody_class(clean_tables):
    waterquality_obj=WaterQualityAdapter(response)
    waterquality=waterquality_obj.run(test_conn, test_cursor)
    assert list(waterquality.__dict__.keys())==["id", "name", "basin", "description",
                                                "water_quality_class", "waterbody_class"]
    assert list(waterquality.__dict__.values())[1:]==["Upper New York Bay",
                                                      "Atlantic Ocean/Long Island Soun",
                                                      "entire bay, as described below", "I",
                                                      "Estuary"]