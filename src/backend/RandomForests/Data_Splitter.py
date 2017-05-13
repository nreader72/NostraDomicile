
# coding: utf-8

# In[21]:

import mysql
import mysql.connector
import pandas as pd
import numpy as np
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
    return str(mean)

def sqFootMean(dataFrame):
    mean = dataFrame['finished_sq_footage'].mean()
    return str(mean)

def homes_bedrooms_df(dataframe):
    df = dataframe.filter(items=['bedrooms'])
    bedList = df['bedrooms'].tolist()
    bedrooms = []
    for x in range(len(bedList)):
        bedrooms.append(bedList[x])
        bedrooms.append(",")
        
    bedrooms = ''.join(str(e) for e in bedrooms)
    return bedrooms

def soldOrNot_addr(dataframe):
    df = dataframe.filter(items=['street_address','sold_binary'])
    addHouse = df['street_address'].tolist()
    binSold = df['sold_binary'].tolist()
    soldOrNotString = []
    for x in range(len(addHouse)):
        soldOrNotString.append(addHouse[x])
        soldOrNotString.append(",")
    soldOrNotString.append("#")
    soldOrNotString.append(',')
    
    for x in range(len(binSold)):
        soldOrNotString.append(binSold[x])
        soldOrNotString.append(",")                           
    
    soldOrNotString = ''.join(str(e) for e in soldOrNotString)
    return soldOrNotString

def house_and_price(dataframe):
    df = dataframe.filter(items=['street_address','last_sale_price'])
    addHouse = df['street_address'].tolist()
    price = df['last_sale_price'].tolist()
    house_price = []
    for x in range(len(addHouse)):
        house_price.append(addHouse[x])
        house_price.append(",")
    house_price.append("#")
    house_price.append(',')
    
    for x in range(len(price)):
        house_price.append(price[x])
        house_price.append(",")                           
    
    house_price = ''.join(str(e) for e in house_price)
    return house_price

# In[ ]:


# In[22]:

def main():
    df = dfMaker('','','',
           '')
    #print(df)
    #print(housePriceMean(df))
    #print(homes_bedrooms_df(df))
    #print(soldOrNot_addr(df))
    print(house_and_price(df))
    
    


# In[7]:

main()


# In[ ]:



