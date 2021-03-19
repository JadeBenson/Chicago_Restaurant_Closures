# localgorithms
CS Winter 2021 Final Project:

Egemen Pamukcu, Jade Benson, Max Kramer, Sabina Hartnett

Libraries & Packages needed: 

csv (0.0.13)
geopandas (0.9.0) - might require geos (0.2.3)
geopy (geopy.distance) (2.1.0)
mapclassify (2.4.2)
matplotlib.pyplot (3.3.4)
numpy (1.20.1)
pandas (1.2.2)
seaborn (0.11.1)
wordcloud (1.8.1)

*Initial Yelp Queries: yapi-collect-searchquery.ipynb*

  Generates a list of coordinates to cover the city of Chicago to catch all businesses 
  Each teammate then ran "get_yelp_query" and "businesses_query" functions on their list of coordinates in stages (to work around API search limit)
  Each teammate combined and then uploaded all their returned buisnesses to the CSVs folder 

*Record Linkage and Data Merging:* 
  **food_inspection_and_linkage.py**
  Subsets the City of Chicago food inspection datasets to identify restaurants before and after COVID
  Queries the Yelp API for the closed and missing businesses
 
 **prepare_data.ipynb**
  Takes in a number of csvs, cleans up the columns to be optimally intuitive and useful and concatenates all the results into a single csv to be used for our visualizations.
  
  
*Visualizing the data: Visualizations.ipynb*

  generates geospatial visualizations of all the open/closed businesses in Chicago and COVID metrics 
  Word clouds and descriptive summaries of businesses (using Yelp data)
  
CSVs folder has all of the CSVs created from running our code
  From the initial Yelp API query: Sabina = "SH_all_business_query", Egemen = "egemen_all", Jade = "all_Jade_data", and Max = "mk_complete"
  From the cleaned food inspection data set: inspections_datasets.zip 
  From the Yelp queries on closed and missing businesses: all_combined_wb.csv
  Final data set (from prepare_data): all_businesses.csv
  
Chicago_Data folder has all of the raw data downloaded from the City of Chicago's data portal 
  boundary geojson file: https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas-current-/cauq-8yn6
  covid geojson file: https://data.cityofchicago.org/Health-Human-Services/COVID-19-Cases-Tests-and-Deaths-by-ZIP-Code/yhhz-zm2v
  food inspection file: https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5/data

Visualizations folder has the images we created to use in the presentation

Deprecated_Code folder has all the old versions of the code before streamlining (kept to demonstrate the process behind this project's creation)
