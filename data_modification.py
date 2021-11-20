import csv
import pandas as pd

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

