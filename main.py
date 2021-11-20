from flask import Flask
import folium

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (60.1666, 24.9436)
    # folium_map = folium.Map(location=start_coords, zoom_start=14)
    # folium.GeoJson("kattavuusdata/4G/4G_tahtiluokka_1.json", name="geojson").add_to(folium_map)
    # folium.GeoJson("kattavuusdata/4G/4G_tahtiluokka_2.json", name="geojson").add_to(folium_map)
    # folium.GeoJson("kattavuusdata/4G/4G_tahtiluokka_3.json", name="geojson").add_to(folium_map)
    import pandas as pd


    state_geo = "postcodes.json"
    state_unemployment = "normalisoitu.csv"
    state_data = pd.read_csv(state_unemployment)

    folium_map = folium.Map(location=[48, -102], zoom_start=3)

    folium.Choropleth(
        geo_data=state_geo,
        name="choropleth",
        data=state_data,
        columns=["Postcode", "Activity"],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Unemployment Rate (%)",
    ).add_to(folium_map)

    folium.LayerControl().add_to(folium_map)
    
    return folium_map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)