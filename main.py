# -*- coding: utf-8 -*-
#! To collect U.S. Newspaper Directory published between 1690-present. This example only collects 1990-2022
#! If there's error, redo the for loop with the new pageID (break point)

import json
import requests
import csv
import pandas as pd
from random import randint
from time import sleep
 
# Returns JSON results
def get_json(url):
    data = requests.get(url)
    return(json.loads(data.content))

# request and collect data 
datacon=pd.DataFrame()
for pageID in range(1,1001):
    url=u"https://chroniclingamerica.loc.gov/search/titles/results/?rows=50&terms=&language=&lccn=&material_type=&year1=1990&year2=2022&labor=&frequency=&ethnicity=&page=%s&sort=relevance&format=json"%pageID
    data = get_json(url)
    df=pd.DataFrame.from_dict(data['items'], orient='columns')
    datacon= pd.concat([datacon,df])
    print('collected page ',pageID)


 

filenamec= 'newspaper_US_directory_chroniclingamerica_1990-2022.csv'
datacon.to_csv(filenamec, encoding='utf-8', header=True)

 
