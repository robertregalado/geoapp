# Boston Crime Map: Insights and Analysis

This code is an example of using the Folium library in Python to create interactive maps visualizing crime data in Boston. Here's a breakdown of what each part does:

1. **Setting up the Environment**: Import necessary libraries such as Pandas for data manipulation, Geopandas for handling geographical data, and Folium for creating interactive maps.

2. **Creating the Basemap**: Initialize a Folium map (`m_1`) with a specified location and zoom level. This map will serve as the base for visualizations.

3. **Loading and Preprocessing Data**: Load crime data from a CSV file, dropping rows with missing location information, and filtering for major crimes occurring in 2018.

4. **Exploring the Data**: Perform some data exploration, such as selecting daytime robberies from the crime dataset.

5. **Visualizing Data on the Map**: Create different visualizations on separate maps (`m_2`, `m_3`, `m_4`, `m_5`, `m_6`) using Folium. These visualizations include:
   - Markers for daytime robberies (`m_2` and `m_3`).
   - Bubble map with varying colors based on the hour of the crime (`m_4`).
   - Heatmap showing the density of crimes (`m_5`).
   - Choropleth map showing the number of crimes in each police district (`m_6`).

Each map is created with specific features and overlays to provide different perspectives on the crime data.

```py
import pandas as pd
import geopandas as gpd
import math
```
