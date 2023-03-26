import requests
import json

from src.fishes import *
fishes

first_fish=fishes[0]
first_fish["Species Name"] #'Crimson Jobfish'
first_fish["Calories"] #'100'
first_fish["Location"]
#'<ul>\n<li>Crimson jobfish are distributed throughout the Indo-Pacific region.
#</li>\n<li>They inhabit hard bottoms at depths from 40 to 120 fathoms.</li>\n</ul>\n'


first_fish_data=location_infos(9.79568, 118.82813, 120)
first_fish_data["salinity"] #{'units': 'g/kg', 'value': None}

oceans=["pacific", "arctic", "atlantic", "indian", "north atlantic", "south atlantic", "indo-pacific"]
coordinates=[{"latitude":8.7832, "longitude":124.5085}]
dict(zip(oceans, coordinates))
location_infos(8.7832, 124.5085, 40)


fishing_vessels=vessel_infos()

first_fish_data=location_infos(-76.611963564, 42.227337, 120)