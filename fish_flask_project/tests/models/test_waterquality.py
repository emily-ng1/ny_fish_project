import pytest
from api.models import Fish, WaterQuality
from api.lib.db import drop_all_tables, test_conn, test_cursor, save


@pytest.fixture()
def fish():
    drop_all_tables(test_conn, test_cursor)

    yield
    drop_all_tables(test_conn, test_cursor)


def test_waterquality_mass_assignment():
    waterquality=WaterQuality(waterbody_class="Ponds", segment_id="0601-0104", win="SR-183-P335", 
                              name="Fox Vly", description="entire lake", basin="Susquehanna River", 
                              part=931, water_quality_class="C")
    assert waterquality.__dict__=={"waterbody_class":"Ponds", "segment_id":"0601-0104", 
                                   "win":"SR-183-P335", "name":"Fox Vly", 
                                   "description":"entire lake", "basin":"Susquehanna River", 
                                   "part":931, "water_quality_class":"C"}
    
def test_save_waterquality():
    waterquality=WaterQuality(waterbody_class="Ponds", segment_id="0601-0104", win="SR-183-P335", 
                              name="Fox Vly", description="entire lake", basin="Susquehanna River", 
                              part=931, water_quality_class="C")
    saved_wq=save(waterquality, test_conn, test_cursor)

    assert type(saved_wq.id)==int
    assert saved_wq.water_quality_class=="C"
