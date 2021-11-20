from flask import Flask
import folium
import pandas as pd
from folium.plugins import MarkerCluster
data_final = pd.read_csv("data/data_final_full.csv")
app = Flask(__name__)

tahtiluokka1 = "data/4G/4G_tahtiluokka_1.json"
tahtiluokka2 = "data/4G/4G_tahtiluokka_2.json"
tahtiluokka3 = "data/4G/4G_tahtiluokka_3.json"

tahtiluokka1_5G = "data/5G/5G_tahtiluokka_1.json"
tahtiluokka2_5G = "data/5G/5G_tahtiluokka_2.json"
tahtiluokka3_5G = "data/5G/5G_tahtiluokka_3.json"

@app.route('/')
def index():
    start_coords = (60.1666, 24.9436)
    folium_map = folium.Map(location=start_coords, zoom_start=6)
    
    state_geo = "data/postcodes.json"
    state_unemployment = "data/normalisoitu.csv"
    state_data = pd.read_csv(state_unemployment)

    folium.Choropleth(
        geo_data=state_geo,
        name="Post code areas",
        data=state_data,
        columns=["Postcode", "Activity"],
        key_on="feature.id",
        bins=9,
        fill_color="YlGnBu",
        fill_opacity=1,
        line_opacity=0,
        line_weight=0,
        line_color="YlGn",
        legend_name="Activity Rate",
        z_index = 0,
        show = True
    ).add_to(folium_map)

    folium.Choropleth(
        geo_data=tahtiluokka1, 
        name="geojson 4G *1",
        fill_color="red",
        fill_opacity=0.7,
        line_color="red",
        line_opacity=0.1,
        z_index = 3,
        show = True
    ).add_to(folium_map)

    folium.Choropleth(
        geo_data=tahtiluokka2, 
        name="geojson 4G *2",
        fill_color="yellow",
        line_color="yellow",
        fill_opacity=0.7,
        line_opacity=0.1,
        z_index = 2,
        show = True
    ).add_to(folium_map)

    folium.Choropleth(
        geo_data=tahtiluokka3, 
        name="geojson 4G *3",
        fill_color="green",
        line_color="green",
        fill_opacity=0.7,
        line_opacity=0.1,
        z_index = 1,
        show = True
    ).add_to(folium_map)


    folium.Choropleth(
        geo_data=tahtiluokka1_5G, 
        name="geojson 5G  *1",
        fill_color="red",
        fill_opacity=0.7,
        line_color="red",
        line_opacity=0.1,
        z_index = 6,
        show = False  
    ).add_to(folium_map)

    folium.Choropleth(
        geo_data=tahtiluokka2_5G, 
        name="geojson 5G *2",
        fill_color="yellow",
        line_color="yellow",
        fill_opacity=0.7,
        line_opacity=0.1,
        z_index = 5,
        show = False
    ).add_to(folium_map)

    folium.Choropleth(
        geo_data=tahtiluokka3_5G, 
        name="geojson 5G *3",
        fill_color="green",
        line_color="green",
        fill_opacity=0.7,
        line_opacity=0.1,
        z_index = 4,
        show = False
    ).add_to(folium_map)
        
    cluster = MarkerCluster(name = "Cell site",
        z_index = 7,
        show = False).add_to(folium_map)
    for index, latlon in data_final.iterrows():
        folium.Marker(location=[latlon["latitude"],latlon["longitude"]],
                            radius=0.0001,
                            weight=5).add_to(cluster)

    folium.LayerControl(autoZIndex=True).add_to(folium_map)
    
    return folium_map._repr_html_()
if __name__ == "__main__":
    app.run(debug=False)