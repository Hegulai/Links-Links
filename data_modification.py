"""
This file is used to clean the cell_zone.csv dataset containing cell sites around finland. It outputs the data_final_full.csv file.
"""

import csv
from os import name
import pandas as pd
import geojson as gj

cz = open("data/cell_zone.csv")
csvreader = csv.reader(cz)

header = []
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)
cz.close()

data = pd.DataFrame(rows, columns = header)
data_tech_long_lat = data[["technology", "latitude", "longitude"]]
data_final = data_tech_long_lat[(data_tech_long_lat["technology"].notnull())]

data_final.to_csv("data/data_final_full.csv", index=False)
