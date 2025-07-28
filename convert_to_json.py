import geopandas as geo
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(BASE_DIR, 'data')

oceans_shp = os.path.join(data_dir, 'World_Seas_IHO_v3.shp')


print("Loading oceans shapefile...")
oceans = geo.read_file(oceans_shp)
oceans['geometry'] = oceans['geometry'].simplify(0.1, preserve_topology=True)
print("Oceans loaded.")

print("Converting and saving oceans to GeoJSON...")
oceans.to_file(os.path.join(data_dir, 'oceans.geojson'), driver='GeoJSON')
print("Oceans saved.")

print("Conversion complete.")
