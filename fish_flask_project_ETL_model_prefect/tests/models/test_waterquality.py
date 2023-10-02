import pytest
from api.models import Fish, WaterQuality
from api.lib.db import drop_all_tables, test_conn, test_cursor, save, find_all


@pytest.fixture()
def clean_tables():
    drop_all_tables(test_conn, test_cursor)

    yield
    drop_all_tables(test_conn, test_cursor)


def test_waterquality_mass_assignment(clean_tables):
    waterquality=WaterQuality(waterbody_class="Ponds",
                              name="Fox Vly", description="entire lake", basin="Susquehanna River", 
                              water_quality_class="C")
    assert waterquality.__dict__=={"waterbody_class":"Ponds", "name":"Fox Vly",
                                   "description":"entire lake", "basin":"Susquehanna River", 
                                   "water_quality_class":"C"}
    
def test_save_waterquality(clean_tables):
    waterquality=WaterQuality(waterbody_class="Ponds", name="Fox Vly", description="entire lake",
                              basin="Susquehanna River", water_quality_class="C")
    saved_wq=save(waterquality, test_conn, test_cursor)

    assert type(saved_wq.id)==int
    assert saved_wq.water_quality_class=="C"

def test_duplicate_waterquality(clean_tables):
    waterquality=WaterQuality(waterbody_class="Ponds", name="Fox Vly", description="entire lake",
                              basin="Susquehanna River", water_quality_class="C")
    saved_wq=save(waterquality, test_conn, test_cursor)

    waterquality=WaterQuality(waterbody_class="Ponds", name="Fox Vly", description="entire lake",
                              basin="Susquehanna River", water_quality_class="C")
    saved_wq=save(waterquality, test_conn, test_cursor)

    wqs=find_all(WaterQuality, test_conn)
    assert [wq.basin for wq in wqs]==["Susquehanna River"]


@pytest.fixture()
def save_waterqualities():
    drop_all_tables(test_conn, test_cursor)

    waterquality_1=WaterQuality(**{"waterbody_class":"Ponds","name":"Fox Vly","description":"entire lake",
                                   "basin":"Susquehanna River","water_quality_class":"C"})
    saved_waterquality_1=save(waterquality_1, test_conn, test_cursor)

    waterquality_2=WaterQuality(**{"waterbody_class":"Ponds","name":"Tully Lake","description":"entire lake",
                                   "basin":"Susquehanna River","water_quality_class":"B"})
    saved_waterquality_2=save(waterquality_2, test_conn, test_cursor)


    yield
    drop_all_tables(test_conn, test_cursor)

def test_find_all_names(save_waterqualities):
    waterqualities=find_all(WaterQuality, test_conn)
    assert [waterquality.name for waterquality in waterqualities]==["Fox Vly", "Tully Lake"]



