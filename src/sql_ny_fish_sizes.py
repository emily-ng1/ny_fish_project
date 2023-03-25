import pandas as pd
import sqlite3

#Convert the json data to CSV
#So I can put it into postgres database and do queries
sizes_df=pd.read_json("https://data.ny.gov/resource/e52k-ymww.json") #Convert json to df using pandas
sizes_df.to_csv("sql_ny_fish_size.csv", index=False) #Convert pandas df to csv file and remove index


#Move data into SQLite3 database
conn=sqlite3.connect("fish_size.db")
cursor=conn.cursor()

url="https://raw.githubusercontent.com/emily-ng1/ny_fish_project/main/sql_ny_fish_size.csv"
fish_sizes_df=pd.read_csv(url)

fish_sizes_df.to_sql("fish_sizes", conn, if_exists="replace") #1000


#Pull up column names
cursor.execute("PRAGMA TABLE_INFO(fish_sizes);")
cursor.fetchall()
# [(0, 'index', 'INTEGER', 0, None, 0),
#  (1, 'year', 'INTEGER', 0, None, 0),
#  (2, 'county', 'TEXT', 0, None, 0),
#  (3, 'waterbody', 'TEXT', 0, None, 0),
#  (4, 'town', 'TEXT', 0, None, 0),
#  (5, 'month', 'TEXT', 0, None, 0),
#  (6, 'number', 'INTEGER', 0, None, 0),
#  (7, 'species', 'TEXT', 0, None, 0),
#  (8, 'size_inches', 'REAL', 0, None, 0)]


#Query questions
#1. Find the fish with the smallest and biggest size
statement='''
SELECT species, size_inches
FROM fish_sizes
ORDER BY size_inches 
LIMIT 1;
'''
cursor.execute(statement)
cursor.fetchall()
#[('Walleye', 0.1)]

statement='''
SELECT species, size_inches
FROM fish_sizes
ORDER BY size_inches DESC
LIMIT 1;
'''
cursor.execute(statement)
cursor.fetchall()
#[('Brown Trout', 24.0)]

#2. Count up fish by species
statement='''
SELECT species, COUNT(*)
FROM fish_sizes
GROUP BY species
ORDER BY COUNT(*) DESC;
'''
cursor.execute(statement)
cursor.fetchall()
# [('Brown Trout', 587),
#  ('Brook Trout', 169),
#  ('Rainbow Trout', 165),
#  ('Walleye', 19),
#  ('Steelhead', 14),
#  ('Muskellunge', 12),
#  ('Landlocked Salmon', 9),
#  ('Lake Trout', 8),
#  ('Round Whitefish', 4),
#  ('Chinook', 4),
#  ('Splake', 3),
#  ('Lake Sturgeon', 2),
#  ('Coho', 2),
#  ('Tiger Muskellunge', 1),
#  ('Sauger', 1)]

#3. Which body of water has the most Brown Trout with the biggest size in year 2021?
statement='''
SELECT *
FROM fish_sizes
WHERE (species="Brown Trout" AND year=2021
AND size_inches=(SELECT size_inches
                 FROM fish_sizes
                 ORDER BY size_inches DESC
                 LIMIT 1))
GROUP BY waterbody
ORDER BY number DESC
LIMIT 1;
'''
cursor.execute(statement)
cursor.fetchall()
# [(420,
#   2021,
#   'Cattaraugus',
#   'Case Lake',
#   'Franklinville',
#   'October',
#   140,
#   'Brown Trout',
#   24.0)]

#4. Which body of water is the smallest fish found for year 2021?
statement='''
SELECT species, size_inches, waterbody
FROM fish_sizes
WHERE year=2021 AND size_inches=(SELECT size_inches
                                 FROM fish_sizes
                                 ORDER BY size_inches
                                 LIMIT 1);
'''
cursor.execute(statement)
cursor.fetchall()
#[('Walleye', 0.1, 'Black Lake')]

#5. Which county has the most vary size for Brown Trout in 2021?
statement='''
SELECT county, species, COUNT(*)
FROM fish_sizes
WHERE year=2021 AND species="Brown Trout"
GROUP BY county, species
ORDER BY COUNT(*) DESC
LIMIT 1;
'''
cursor.execute(statement)
cursor.fetchall()
#[('Delaware', 'Brown Trout', 82)]





