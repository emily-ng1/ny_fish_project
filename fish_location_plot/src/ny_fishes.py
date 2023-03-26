import requests
import folium
import webbrowser


#{'location': {'latitude': '44.918344554', 'needs_recoding': False, 'longitude': '-74.293337254'},
# 'point_y': '44.918344554',
# ':@computed_region_yamh_8v7k': '188',
# 'name': 'Trout River',
# 'comments': 'None',
# 'point_x': '-74.293337254',
# ':@computed_region_wbg7_3whc': '218',
# 'fish_spec': 'Brown Trout*',
# ':@computed_region_kjdx_g34t': '621',
# 'spec_regs': {'url': 'http://www.dec.ny.gov/outdoor/31444.html'},
# 'county': 'Franklin'}



#Import NY fishes data set
def get_fish_data():
    url = "https://data.ny.gov/resource/tjny-fki3.json"
    response = requests.get(url)
    fishes = response.json()
    return fishes

#Get a list of unique fishes in NY
def fish_species(fishes):
    all_species=[fish["fish_spec"] for fish in fishes]
    unique_fishes=list(set(all_species))
    return sorted(unique_fishes)

#Get List of unque fish species
fishes=get_fish_data()
unique_fish_species=fish_species(fishes)


#Look at the data by waterbody
def request_by_waterbody(waterbody):
    waterbody=waterbody.title()
    waterbody_url=f"https://data.ny.gov/resource/tjny-fki3.json?name={waterbody}"
    response=requests.get(waterbody_url)
    results=response.json()
    return results

black_river=request_by_waterbody("black river")
len(black_river) #18


#Plot all the fish species present at the Black River waterbody
#name, fish_spec, location(latitude, longitude), county
def extract_details_from_fishes(fishes):
    fishes_clean=[]

    for fish in fishes:
        name=fish["name"]
        species=fish["fish_spec"]
        latitude=fish["point_y"]
        longitude=fish["point_x"]
        county=fish["county"]

        fishes_clean.append({"name":name, "fish_species_present":species, "location":[latitude, longitude], "county":county})
    return fishes_clean

extracted_fishes=extract_details_from_fishes(fishes)


#Get fishes data from Black River only
def fishes_in_black_river(extracted_fishes):
    return [fish for fish in extracted_fishes if fish["name"]=="Black River"]

fishes_black_river=fishes_in_black_river(extracted_fishes)
len(fishes_black_river) #18


#Plot the data using folium
def plot_fishes_in_black_river(extracted_fishes):
    fishes=fishes_in_black_river(extracted_fishes)

    black_river_location=[44.0126, 75.7944]
    black_river_map=folium.Map(location=black_river_location, zoom_start=2)
    for fish in fishes:
        folium.Marker(location=fish["location"], popup=fish["fish_species_present"]).add_to(black_river_map)

    output_file="map.html"
    black_river_map.save(output_file)

    return webbrowser.open(output_file)

plot_fishes_in_black_river(extracted_fishes)














