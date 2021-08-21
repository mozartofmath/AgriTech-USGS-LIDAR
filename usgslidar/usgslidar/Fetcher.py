import json
import logging
#import pdal

class Fetcher:
    def __init__(self):
        filename = 'pipeline.json'
        try:
            f = open(filename, 'r')
        except FileNotFoundError:
            print('Error: JSON File not Found')
            logging.error('JSON File not Found')
        self.pipeline = json.load(f)
        f.close()
        
    def set_boundary(self, xmin : float, xmax : float, ymin : float, ymax : float) -> None:
        """
        Set the boundary of the area you want to fetch the LIDAR data for
        """
        self.pipeline['pipeline'][0]['bounds'] = f"([{xmin}, {xmax}], [{ymin}, {ymax}])"
        logging.info('set boundary')
        
    def set_region(self, region : str) -> None:
        """
        Set the region you want to fetch the LIDAR data for
        """
        split = self.pipeline['pipeline'][0]['filename'].split('/')
        split[-2] = region
        self.pipeline['pipeline'][0]['filename'] = '/'.join(split)
        
    def set_out_filename(self, name : str) -> None:
        """
        Set the filenames for the output .laz and .tif files
        """
        self.pipeline['pipeline'][4]['filename'] = f"{name}.laz"
        self.pipeline['pipeline'][5]['filename'] = f"{name}.tif"
        logging.info('set output file names')
    
    def fetch(self):
        """
        execute pipeline and fetch data
        """
        PIPE = pdal.Pipeline(self.pipeline)
        pipeline.execute()
        logging.info('LIDAR Data Fetched')