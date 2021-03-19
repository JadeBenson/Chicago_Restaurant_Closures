# localgorithms
CS Winter 2021 Final Project:
Egemen Pamukcu, Jade Benson, Max Kramer, Sabina Hartnett

Libraries & Packages needed: 
Geopy (geopy.distance)
numpy 
pandas 
csv
copy
geopandas 
matplotlib.pyplot 
mapclassify 
seaborn 
wordcloud

Begin with yapi-collect-searchquery
  Generates a list of coordinates to cover the city of Chicago to catch all businesses 
  Each teammate then ran "get_businesses" function on their list of coordinates in stages (to work around API search limit)
  Each teammate combined and then uploaded all their returned buisnesses to the CSVs folder (Sabina = "SH_all_business_query", Egemen = "egemen_all", Jade = "all_Jade_data", and Max = "mk_complete")   
  
End with Visualizations 
  generates geospatial visualizations of all the open/closed businesses in Chicago and COVID metrics 
  Word clouds and descriptive summaries of businesses (using Yelp data) 
  
Chicago_Data folder has all of the raw data downloaded from the City of Chicago's data portal 
boundary geojson file: https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas-current-/cauq-8yn6
covid geojson file: https://data.cityofchicago.org/Health-Human-Services/COVID-19-Cases-Tests-and-Deaths-by-ZIP-Code/yhhz-zm2v
food inspection file: https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5/data

Visualizations folder has the images we created to use in the presentation 
