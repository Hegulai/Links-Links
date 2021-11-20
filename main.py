from flask import Flask
import folium
import pandas as pd

data_final = pd.read_csv("data_final.csv")
app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (60.1666, 24.9436)
    folium_map = folium.Map(location=start_coords, zoom_start=6)
    for index, latlon in data_final.iterrows():
        folium.CircleMarker(location=[latlon["latitude"],latlon["longitude"]],
                            radius=0.0001,
                            weight=5).add_to(folium_map)

    tahtiluokka1 = "kattavuusdata/4G/4G_tahtiluokka_1.json"
    tahtiluokka2 = "kattavuusdata/4G/4G_tahtiluokka_2.json"
    tahtiluokka3 = "kattavuusdata/4G/4G_tahtiluokka_3.json"
    folium.Choropleth(
        geo_data=tahtiluokka1, 
        name="geojson",
        fill_color="red",
        fill_opacity=0.7,
        line_color="red",
        line_opacity=0.1
    ).add_to(folium_map)
    folium.Choropleth(
        geo_data=tahtiluokka2, 
        name="geojson",
        fill_color="yellow",
        line_color="yellow",
        fill_opacity=0.7,
        line_opacity=0.1
    ).add_to(folium_map)
    folium.Choropleth(
        geo_data=tahtiluokka3, 
        name="geojson",
        fill_color="green",
        line_color="green",
        fill_opacity=0.7,
        line_opacity=0.1
    ).add_to(folium_map)
    
    return folium_map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)