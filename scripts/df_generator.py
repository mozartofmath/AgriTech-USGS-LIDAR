import numpy as np
import pylas
from shapely.geometry import Point
import geopandas
import logging

class GenerateDF:
    def generate_df(self, filepath : str, coordinate_system : int):
        """
        Takes in the path to the .laz/.las file along with the coordinate system and returns a 
        geopandas dataframe
        """
        try:
            fh = pylas.open(filepath)
        except FileNotFoundError:
            print(f'Error: file {filepath} not Found')
            logging.error(f'Error: file {filepath} not Found')
        las = fh.read()
        p_X = las.x
        p_Y = las.y
        p_Z = las.z
        classification = las.classification
        d = {'elevation_m': p_Z, 'classification': classification, 'geometry': [Point(x,y) for x,y in zip(p_X,p_Y)]}
        gdf = geopandas.GeoDataFrame(d, crs=f"EPSG:{coordinate_system}")
        return gdf