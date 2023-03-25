import pandas as pd

#Convert the json data to CSV
#So I can put it into postgres database and do queries
fish_size_df=pd.read_json("https://data.ny.gov/resource/e52k-ymww.json") #Convert json to df using pandas
fish_size_df.to_csv("sql_ny_fish_size.csv", index=False) #Convert pandas df to csv file and remove index

#Move data into SQLite3 database
url="https://raw.githubusercontent.com/emily-ng1/flask_project_lab/main/grades.csv"
sample=pd.read_csv(url)

