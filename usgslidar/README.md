# AgriTech - USGS LIDAR
## Introduction
<p>
This package contains all the tools you need to download LiDAR data for any area in the USGS 3DEP dataset and visualize it.
</p>
<p>
GIS or geographic information system is a computer system that allows for visualizing, manipulating, capturing, and storage of data with associated attributes. GIS offers better understanding of patterns and relationships of the landscape at different scales. Tools inside the GIS allow for manipulation of data for spatial analysis or cartography.
</p>
<p>
Height Map of Earth's surface (including water and ice) in equirectangular projection, normalized as 8-bit gray scale, where lighter values indicate higher elevation. A topographical map is the main type of map used to depict elevation, often through use of contour lines. In a Geographic Information System (GIS), digital elevation models (DEM) are commonly used to represent the surface (topography) of a place, through a raster (grid) dataset of elevations. Digital terrain models are another way to represent terrain in GIS. 
</p>
<p>
USGS (United States Geologic Survey) is developing a 3D Elevation Program (3DEP) to keep up with growing needs for high quality topographic data. 3DEP is a collection of enhanced elevation data in the form of high quality LiDAR data over the conterminous United States, Hawaii, and the U.S. territories. There are three bare earth DEM layers in 3DEP which are nationally seamless at the resolution of 1/3, 1, and 2 arcseconds.
</p>

## Getting Started
<p>
To install the package type the following commands
</p>
```
	git clone https://github.com/mozartofmath/AgriTech-USGS-LIDAR.git
	cd AgriTech-USGS-LIDAR/usgslidar
	pip install .
```

## Code
The code of our analysis can be found in the **notebooks** folder. The data loading and visualization can be found in the **Fetcher.ipynb** jupyter notebook. The **scripts** folder contains the data loading and preprocessing functions.

## Dependencies
To install the necessary dependencies, execute the command 
```$ pip install -r requirements.txt```
