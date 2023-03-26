import requests
import plotly.graph_objects as go

#Show the plot of the average fish size


#{'year': '2021',
# 'county': 'Warren',
# 'waterbody': 'Accessible Pond 1',
# 'town': 'Hatchery',
# 'month': 'April',
# 'number': '30',
# 'species': 'Rainbow Trout',
# 'size_inches': '9.5'}


#Import fish size json data
def get_fish_size_data():
    url="https://data.ny.gov/resource/e52k-ymww.json"
    response = requests.get(url)
    fishes_size = response.json()
    return fishes_size

fishes_size=get_fish_size_data()

#Get the list of unique fish
def unique_fish_size_species(fishes_size):
    all_species=[fish["species"] for fish in fishes_size]
    unique_fishes=list(set(all_species))
    return sorted(unique_fishes)

unique_fish=unique_fish_size_species(fishes_size)

#Get all species fish with their avg size
def calc_fish_avg_size(unique_fish, fishes_size):
    avg_size=[]
    for fish in unique_fish:
        size_sum=0
        count=0
        for dict in fishes_size:
            if fish in dict["species"]:
                size_sum=size_sum+float(dict["size_inches"])
                count=count+1
        avg_size.append({"species":fish, "avg_size_inches":round(size_sum/count, 2)})
    return avg_size

fish_avg_size_inches=calc_fish_avg_size(unique_fish, fishes_size)

#Plot the fish species with it's avg size
species=[fish["species"] for fish in fish_avg_size_inches]
avg_size_inches=[fish["avg_size_inches"] for fish in fish_avg_size_inches]

scatter=go.Scatter(y=avg_size_inches, mode="markers", hovertext=species)
fig=go.Figure(scatter)
fig.update_xaxes(title_text="Fish")
fig.update_yaxes(title_text="Average size")
fig.show("browser")