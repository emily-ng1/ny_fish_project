from api.models.ny_fish import Fish
from api.lib.db import save


class FishAdapter:
    def __init__(self, response_fish):
        self.response_fish=response_fish

    def select_attributes(self):
        waterbody=self.response_fish["waterbody"]
        species=self.response_fish["species"]
        size_inches=self.response_fish["size_inches"]
        number=self.response_fish["number"]
        month=self.response_fish["month"]
        year=self.response_fish["year"]

        keys=["waterbody", "species", "size_inches", "number", "month", "year"]
        vals=[waterbody, species, size_inches, number, month, year]
        attr=dict(zip(keys, vals))
        return attr

    def run(self, conn, cursor):
        attrs=self.select_attributes()
        fish_obj=Fish(**attrs)
        #fish=save(fish_obj, conn, cursor)
        return fish_obj
