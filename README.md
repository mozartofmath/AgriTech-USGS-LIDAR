# AgriTech - USGS LIDAR
## Introduction
<p> At AgriTech, we are very interested in how water flows through a maize farm field. This knowledge will help us improve our research on new agricultural products being tested on farms.

How much maize a field produces is very spatially variable. Even if the same farming practices, seeds and fertilizer are applied exactly the same by machinery over a field, there can be a very large harvest at one corner and a low harvest at another corner.  We would like to be able to better understand which parts of the farm are likely to produce more or less maize, so that if we try a new fertilizer on part of this farm, we have more confidence that any differences in the maize harvest 9are due mostly to the new fertilizer changes, and not just random effects due to other environmental factors.  
 </p>

## Code
The code of our analysis can be found in the **notebooks** folder. The data loading and visualization can be found in the **Fetcher.ipynb** jupyter notebook. The **scripts** folder contains the data loading and preprocessing functions. 
## pip installable package
The pip installable module along with a more deailed `README` and `tutorials` can be found in the **usgslidar** directory. 
<p>
To install the package type the following commands
</p>

```
git clone https://github.com/mozartofmath/AgriTech-USGS-LIDAR.git
cd AgriTech-USGS-LIDAR/usgslidar
pip install .
```

## Dependencies
To install the necessary dependencies, execute the command 
```$ pip install -r requirements.txt"```
