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
pip install -r requirements.txt
pip install .
```

## Tutorial
### 1. Fetch LiDAR data
The boundary of the area is of the form `xmin, xmax, ymin, ymax`.
This area is located in Iowa State. Therefore, we set the region as `“IA_FullState”`
Then we set the filename of the output `.tif` and `.laz` files as `“iowa”`

```python
from usgslidar.Fetcher import Fetcher
fetcher = Fetcher()
fetcher.set_boundary(-10425171.940, -10423171.940, 5164494.710, 5166494.710)
fetcher.set_region('IA_FullState')
fetcher.set_out_filename('iowa')
fetcher.fetch()
```

### 2. Visualize 
The plot function in the Visualizer module takes in the path to the `.tif` file 
along with the `title` of the plot as input and plots it.


```python
from usgslidar.Visualizer import Visualizer
vis = Visualizer()
vis.plot("../iowa.tif", "Iowa")
```

### 3. Convert data to geopandas dataframe
You can turn a `.laz` or `.las` file into a geopandas dataframe by using the GenerateDF module.


```python
from usgslidar.df_generator import GenerateDF
gen = GenerateDF()
#inputs are the path to the .laz/.las file and the coordinate system
geo_df = gen.generate_df('../iowa.laz', 26915)
geo_df.head()
```

