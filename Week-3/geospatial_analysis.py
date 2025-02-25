import geopandas as gpd
import folium

# Download the dataset manually from Natural Earth: 
# https://www.naturalearthdata.com/downloads/110m-cultural-vectors/

# Load the dataset from a local path (Update with your actual path)
world = gpd.read_file("F:/EDA/Week-3/datasets/ne_110m_admin_0_countries.shp")

# Create a map centered at a specific location
map = folium.Map(location=[20, 0], zoom_start=2)

# Add country boundaries to the map
for _, row in world.iterrows():
    folium.Marker(
        location=[row.geometry.centroid.y, row.geometry.centroid.x],
        popup=row["NAME"]
    ).add_to(map)

# Save the map to an HTML file
map.save("geospatial_map.html")

print("Geospatial analysis completed successfully. Open 'geospatial_map.html' to view the map.")
