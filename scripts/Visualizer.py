import rasterio
import rasterio.plot
import matplotlib.pyplot as plt
class Visualizer:
    def plot(self, filename : str, title : str):
        """
        Takes in the filename to the .tif file, and the title to the plot
        as input and plots it.
        """
        tif = rasterio.open(filename)
        fig, axes = plt.subplots(figsize=(12,12))
        rasterio.plot.show(tif, title = title)