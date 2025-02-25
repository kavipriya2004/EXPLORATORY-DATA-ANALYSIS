import geopandas as gpd
import folium

# Load World Map Dataset 
world = gpd.read_file("F:/EDA/Week-4/datasets/ne_110m_admin_0_countries.shp")

# Create a World Map Visualization
world_map = folium.Map(location=[20, 0], zoom_start=2)
folium.GeoJson(world, name="World Countries").add_to(world_map)
world_map.save("world_map.html")  

print("✅ World Map Saved as world_map.html")

# Load India States Dataset 
india_states = gpd.read_file("F:/EDA/Week-4/datasets/gadm41_IND_1.shp")

# Create India States Map
india_map = folium.Map(location=[20.5, 78.9], zoom_start=5)
folium.GeoJson(india_states, name="India States").add_to(india_map)
india_map.save("india_states_map.html")  

print("✅ India States Map Saved as india_states_map.html")

# Load India Districts Dataset 
india_districts = gpd.read_file("F:/EDA/Week-4/datasets/gadm41_IND_3.shp")

# Create India Districts Map
district_map = folium.Map(location=[20.5, 78.9], zoom_start=5)
folium.GeoJson(india_districts, name="India Districts").add_to(district_map)
district_map.save("india_districts_map.html")  

print("✅ India Districts Map Saved as india_districts_map.html")
