from flask import Flask
import folium

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (60.1666, 24.9436)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    folium.GeoJson("kattavuusdata/4G/4G_tahtiluokka_1.json", name="geojson").add_to(folium_map)
    folium.GeoJson("kattavuusdata/4G/4G_tahtiluokka_2.json", name="geojson").add_to(folium_map)
    folium.GeoJson("kattavuusdata/4G/4G_tahtiluokka_3.json", name="geojson").add_to(folium_map)
    
    
    return folium_map._repr_html_()

if __name__ == "__main__":
    app.run(debug=True)