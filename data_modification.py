import csv
from os import name
import pandas as pd
import geojson as gj

cz = open("cell_zone.csv")
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
data_final = data_final[((pd.to_numeric(data_final["longitude"]) > 23.97) & (pd.to_numeric(data_final["latitude"]) < 60.40) & (pd.to_numeric(data_final["longitude"]) < 25.47))]

data_final.to_csv("data_final.csv", index=False)

# Iteroidaan kaikki json alueet ja sit poistetaan ne palikat joissa on jokin piste alueen ulkopuolella

tahtiluokka1 = "kattavuusdata/4G/4G_tahtiluokka_1.json"
tahtiluokka2 = "kattavuusdata/4G/4G_tahtiluokka_2.json"
tahtiluokka3 = "kattavuusdata/4G/4G_tahtiluokka_3.json"

files_4g = [tahtiluokka1] #, tahtiluokka2, tahtiluokka3]

for file in files_4g:
    with open(file) as f:
        stuff = gj.load(f)
    
    for feature in stuff["features"]:
        is_not_a_ok_polygon = False
        for point in feature["geometry"]["coordinates"][0]:
            if (point[0] < 23.97) or (point[0] > 25.47) or (point[1] > 60.40):
                is_ok_polygon = True
                break
        if is_not_a_ok_polygon:
            print("hei!")