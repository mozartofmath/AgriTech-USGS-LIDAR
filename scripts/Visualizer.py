import rasterio
import rasterio.plot
import matplotlib.pyplot as plt
import logging
class Visualizer:
    def plot(self, filename : str, title : str):
        """
        Takes in the filename to the .tif file, and the title to the plot
        as input and plots it.
        """
        try:
            tif = rasterio.open(filename)
        except FileNotFoundError:
            print(f'Error: file {filepath} not Found')
            logging.error(f'Error: file {filepath} not Found')
        fig, axes = plt.subplots(figsize=(12,12))
        rasterio.plot.show(tif, title = title)