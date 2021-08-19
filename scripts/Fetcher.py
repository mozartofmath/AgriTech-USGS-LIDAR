import json
import logging
#import pdal

class Fetcher:
    def __init__(self):
        filename = '../pipeline.json'
        try:
            f = open(filename, 'r')
        except FileNotFoundError:
            print('json File not Found')
            logging.info('json File not Found')
        self.pipeline = json.load(f)
        
    def set_boundary(self, xmin, xmax, ymin, ymax):
        self.pipeline['pipeline'][0]['bounds'] = f"([{xmin}, {xmax}], [{ymin}, {ymax}])"
        logging.info('set boundary')
        
    def set_region(self, region):
        split = self.pipeline['pipeline'][0]['filename'].split('/')
        split[-2] = region
        self.pipeline['pipeline'][0]['filename'] = '/'.join(split)
        
    def set_out_filename(self, name):
        self.pipeline['pipeline'][4]['filename'] = f"{name}.laz"
        self.pipeline['pipeline'][5]['filename'] = f"{name}.tif"
        logging.info('set output file names')
    
    def fetch(self):
        PIPE = pdal.Pipeline(self.pipeline)
        pipeline.execute()
        logging.info('LIDAR Data Fetched')