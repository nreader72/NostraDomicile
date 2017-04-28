
# coding: utf-8

# In[16]:

import mysql
import mysql.connector
import pandas as pd
import numpy as np
import json  
 
#import plotly.tools as tls
#tls.embed('https://plot.ly/~cufflinks/8')


# In[6]:

def dfMaker(user,password,host,database,zipCode):
    cnx = mysql.connector.connect(user=user,password=password,
                                  host=host,database=database)
    cursor = cnx.cursor()
    df = pd.read_sql('SELECT*FROM PyZillow_Data.home_data Where zip =' + zipCode, con=cnx)
    return df

def housePriceMean(dataFrame):
    mean = dataFrame['last_sale_price'].mean()
    mean = json.dumps(mean)
    mean = json.loads(mean)
    return mean

def sqFootMean(dataFrame):
    mean = dataFrame['finished_sq_footage'].mean()
    mean = json.dumps(mean)
    mean = json.loads(mean)
    return mean

def homes_bedrooms_df(dataframe):
    df = dataframe.filter(items=['bedrooms'])
    df = df.to_json(orient='columns')
    return df

def soldOrNot_addr(dataframe):
    df = dataframe.filter(items=['street_address','sold_binary'])
    df = df.to_json(orient='columns')
    return df

def allData():
    df = dfMaker('ctsimaan','SeniorProject490','nostradomicile-data.c6x7vypetdqh.us-west-2.rds.amazonaws.com','PyZillow_Data','27705')
    return_data = {}
    return_data['housePriceMean'] = housePriceMean(df)
    return_data['sqFootMean'] = sqFootMean(df)
    return_data['homes_bedrooms_df'] = homes_bedrooms_df(df)
    return_data['soldOrNot_addr'] = soldOrNot_addr(df)
    return_data = json.dumps(return_data)
    return return_data



    #print(df)
    #print(housePriceMean(df))
    #print(homes_bedrooms_df(df))
#print(allData())
    


# In[ ]:



