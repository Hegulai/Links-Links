from flask import Flask
import folium
import pandas as pd
from folium.plugins import MarkerCluster
from folium.features import DivIcon
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
    season_activity_change = "data/holiday_season_activity2.csv"
    season_data = pd.read_csv(season_activity_change)
    christmas_activity_change = "data/christmas_activity2.csv"
    christmas_data = pd.read_csv(season_activity_change)


    folium.Choropleth(
        geo_data=state_geo,
        name="Movement activity by post code",
        data=state_data,
        columns=["Postcode", "Activity"],
        key_on="feature.id",
        bins=9,
        fill_color="YlGnBu",
        fill_opacity=1,
        line_opacity=0,
        line_weight=0,
        line_color="YlGn",
        show = True,
        legend_name="Movement activity"
    ).add_to(folium_map)

    folium.Choropleth(
        geo_data=state_geo,
        name="Movement activity change from November to July by post code",
        data=season_data,
        columns=["Postcode", "Activity"],
        key_on="feature.id",
        bins=9,
        fill_color="RdPu",
        fill_opacity=1,
        line_opacity=0,
        line_weight=0,
        line_color="YlGn",
        legend_name="Movement activity change (November to July)",
    ).add_to(folium_map)

    folium.Choropleth(
        geo_data=state_geo,
        name="Movement activity change from Christmas to Monday Nov. 4th by post code",
        data=christmas_data,
        columns=["Postcode", "Activity"],
        key_on="feature.id",
        bins=9,
        fill_color="PuBuGn",
        fill_opacity=1,
        line_opacity=0,
        line_weight=0,
        line_color="YlGn",
        legend_name="Movement activity change (Christmas Day to Nov 4th)",
    ).add_to(folium_map)

    cluster = MarkerCluster(name = "Cell site").add_to(folium_map)
    for index, latlon in data_final.iterrows():
        folium.Marker(location=[latlon["latitude"],latlon["longitude"]],
                            radius=0.0001,
                            weight=5).add_to(cluster)

    folium.Choropleth(
        geo_data=tahtiluokka1, 
        name="4G *1",
        fill_color="red",
        fill_opacity=0.7,
        line_color="red",
        line_opacity=0.1,
        show = True
    ).add_to(folium_map)

    folium.Choropleth(
        geo_data=tahtiluokka2, 
        name="4G *2",
        fill_color="yellow",
        line_color="yellow",
        fill_opacity=0.7,
        line_opacity=0.1,
        show = True
    ).add_to(folium_map)

    folium.Choropleth(
        geo_data=tahtiluokka3, 
        name="4G *3",
        fill_color="green",
        line_color="green",
        fill_opacity=0.7,
        line_opacity=0.1,
        show = True
    ).add_to(folium_map)


    folium.Choropleth(
        geo_data=tahtiluokka1_5G, 
        name="5G  *1",
        fill_color="red",
        fill_opacity=0.7,
        line_color="red",
        line_opacity=0.1,
        show = False  
    ).add_to(folium_map)

    folium.Choropleth(
        geo_data=tahtiluokka2_5G, 
        name="5G *2",
        fill_color="yellow",
        line_color="yellow",
        fill_opacity=0.7,
        line_opacity=0.1,
        show = False
    ).add_to(folium_map)

    folium.Choropleth(
        geo_data=tahtiluokka3_5G, 
        name="5G *3",
        fill_color="green",
        line_color="green",
        fill_opacity=0.7,
        line_opacity=0.1,
        show = False
    ).add_to(folium_map)
        
    cluster = MarkerCluster(name = "Cell site",
        z_index = 7,
        show = False).add_to(folium_map)
    for index, latlon in data_final.iterrows():
        folium.Marker(location=[latlon["latitude"],latlon["longitude"]],
                            radius=0.0001,
                            weight=5).add_to(cluster)


    folium.map.Marker(
    [59.5, 22],
    icon=DivIcon(
        icon_size=(700,400),
        icon_anchor=(0,0),
        html='<div style="font-size: 20pt">Movement decrease from November to July: -64.5%</div><div style="font-size: 20pt">Base station power consumption save: 5.9%</div><div style="font-size: 20pt">Network power consumption save: 5.0%</div><div style="font-size: 20pt"> Operating cost save: 1.5%</div>',
        ),
        show = True
    ).add_to(folium_map)

    folium.LayerControl().add_to(folium_map)
    
    return folium_map._repr_html_()
if __name__ == "__main__":
    app.run(debug=False)