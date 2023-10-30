import pyproj
import pandas as pd
import geopandas as gpd


def osgb_to_lonlat(dfr):
    dfr = dfr.reset_index()
    transformer = pyproj.Transformer.from_crs("EPSG:27700", "EPSG:4326", always_xy=True)
    dfr["longitude"], dfr["latitude"] = transformer.transform(dfr["x"], dfr["y"])
    dfr = dfr.drop(["x", "y"], axis=1)
    return dfr


def get_UK_climate_region(dfr):
    """Determine MetOffice Hadley precipitatino region for locations in DataFrame"""
    regions = gpd.read_file("/Users/tadas/modFire/fire_lc_ndvi/data/HadUKP_regions.shp")
    regions = regions.set_crs("EPSG:27700")
    regions = regions.to_crs("EPSG:4326")
    geometry = gpd.points_from_xy(dfr.longitude, dfr.latitude)
    gdf = gpd.GeoDataFrame(dfr, geometry=geometry, crs=4326)
    pts = gpd.sjoin(regions, gdf)
    pts = pts.drop(["geometry", "index_right"], axis=1)
    df = pd.DataFrame(pts)
    return df
