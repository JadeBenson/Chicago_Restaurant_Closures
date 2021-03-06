from yelpapi import YelpAPI
import pandas as pd
import numpy as np
import requests 
import json
import csv
from tqdm import tqdm # progress bar

'''
Partition the Food Inspection dataset into component CSVs for record linkage
J. Benson
'''
food_inspect = pd.read_csv("Food_Inspections.csv")
food_inspect['Inspection Date'] = pd.to_datetime(food_inspect['Inspection Date'])

before_covid = food_inspect[food_inspect['Inspection Date'] > '2019-01-01']
before_covid = before_covid[before_covid["Inspection Date"] < "2020-03-01"]
before_covid = before_covid.sort_values(by = ["Inspection Date"])
before_covid = before_covid.drop(columns = ["Inspection ID", "License #", "Risk", "City", "State"])
before_covid = before_covid.drop_duplicates('DBA Name', keep='first')
before_covid.to_csv("before_covid.csv")

after_covid = food_inspect[food_inspect['Inspection Date'] > '2020-03-01']
after_covid = after_covid.sort_values(by = ["Inspection Date"])
after_covid = after_covid.drop(columns = ["Inspection ID", "License #", "Risk", "City", "State"])
after_covid = after_covid.drop_duplicates('DBA Name', keep='first')
after_covid.to_csv("after_covid.csv")

now_closed = after_covid[after_covid.Results == "Out of Business"]
now_closed.to_csv("now_closed.csv")

merged_closed = now_closed.merge(before_covid, how='left', on= "DBA Name", suffixes = ("_after", "_before"))
merged_all = before_covid.merge(after_covid, how='outer', on= "DBA Name", suffixes = ("_before", "_after"))
merged_all.to_csv("merged_all.csv")

missing_after = merged_all[merged_all['Results_after'].isna()]
missing_after.to_csv("missing_after.csv")

unique_rest = food_inspect.drop_duplicates('DBA Name', keep='first')


'''
Link the food inspection data to the Yelp Fusion API 
M. Kramer
'''

# Change to your api key
key = '50G0TnHbhsICvJWfMYhAHwaWs1TVwxf0hDrp0QF3rN1cHVvSH5Lkh0g2y_VysxT1T_H9bIm_t1JultXGfpy2z0ewPCJh9GgOtdgE_wKaNlGY-SDaKDmRuYPJDz4sYHYx'
# Change to the dataset you want to run
path_to_data = "now_closed.csv" 
    
def gen_params(dataset,rownum):
    '''
    generates query parameters for a business in the df
    '''
    business = dataset.iloc[rownum] # get the business from the data
    name = str(business['AKA Name']).lower() # food inspection is all upper, yelp is all lower.
    address1 = str(business['Address']) # only need street address for match endpoint
    return (name,address1)

def query_businesses(apikey,path_to_data,outfile_name):
    '''
    Main function. Perform matching and detail querying. Calls gen_params
    '''
    data = pd.read_csv(path_to_data) # load in the data
    outlist = []
    nomatch_counter = 0
    match_counter = 0
    for i in tqdm(range(len(data))): # test every business in the dataset
        (name,address1) = gen_params(data,i) # generate matching parameters
        headers = {'Authorization': 'Bearer %s' % apikey}
        match_url = "https://api.yelp.com/v3/businesses/matches"
        match_params = {'name': name, 'address1' : address1, 'city' : 'chicago', 'state' : 'IL','country' : "US"}
    
        req = requests.get(match_url, headers=headers, params=match_params) # business match endpoint call
        jstext = json.loads(req.text) # load result into JSON
    
    
        if jstext['businesses'] == []: # check if business returns from match call
            nomatch_counter += 1
            continue
        
        # MATCH FOUND, find details
        match_counter += 1 
        id = jstext['businesses'][0]['id'] # get the yelp id of the business if it matches
        details_params = {'limit' : 1} # only return 1 business
        details_url = "https://api.yelp.com/v3/businesses/%s" % id # prepare business search endpoint 
        
        result = requests.get(details_url,headers=headers,params=details_params) # business search endpoint call
        jstext = json.loads(result.text) # load result into JSON
        outlist.append(jstext)
    print("matches: %s" % match_counter)
    print("failed to match: %s" % nomatch_counter)
    df = pd.DataFrame(outlist) # create df from outlist
    df.to_csv(outfile_name)

query_businesses(key,path_to_data,"results_from_record_linking.csv") # Run Script