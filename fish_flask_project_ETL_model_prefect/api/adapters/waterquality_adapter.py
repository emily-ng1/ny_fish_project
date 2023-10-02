from api.models.ny_water_quality import WaterQuality
from api.lib.db import save


class WaterQualityAdapter:
    def __init__(self, response_waterquality):
        self.response_waterquality=response_waterquality

    def selected_attributes(self):
        attrs=["name", "basin", "description", "water_quality_class", "waterbody_class"]
        return {attr:self.response_waterquality[attr] for attr in attrs}

    def run(self, conn, cursor):
        attrs=self.selected_attributes()
        waterquality_obj=WaterQuality(**attrs)
        waterquality=save(waterquality_obj, conn, cursor)
        return waterquality


