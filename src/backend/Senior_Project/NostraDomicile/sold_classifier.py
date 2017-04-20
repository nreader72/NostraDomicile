# Code written by Jeremy Hutton - copied to new location for testing
# coding: utf-8

# In[ ]:

#import mysql
#import mysql.connector
#import csv
#import pandas as pd
#import numpy as np
#import scipy
#from sklearn import model_selection
#from sklearn.model_selection import train_test_split
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.metrics import precision_recall_fscore_support


#zip code for this is 27705
def sold_classifier(zip_code):
    cnx = mysql.connector.connect(user='ctsimaan',password='SeniorProject490',
                              host='nostradomicile-data.c6x7vypetdqh.us-west-2.rds.amazonaws.com',
                              database='PyZillow_Data')
    cursor = cnx.cursor()

###################

    df_pd = pd.read_sql('SELECT*FROM PyZillow_Data.home_data Where zip = ' + zip_code, con=cnx)
    frames = [df_pd,df_pd]
    df_pd = pd.concat(frames)

####################

    new = df_pd.filter(['sold_binary', 'home_type', 'bedrooms', 'bathrooms', 'finished_sq_footage',
       'lot_size_sq_footage','year_built','last_sale_price','neighborhood', 'school_district'], axis = 1)
    #d = {'sold_binary':0, 'bedrooms':5,'bathrooms':3,'finished_sq_footage':2000,
         #'lot_size_sq_footage':7405.0,'year_built':1990, 'last_sale_price':250000.0,'home_type':"SingleFamily",'neighborhood':
        #None, 'school_district':None}
    #d = pd.DataFrame(data = d, index=[356])
    #addData = [new,d]
    #new = pd.concat(addData)
    df = pd.DataFrame(data = new)
    cols_to_transform = [ 'home_type','neighborhood','school_district']
    df_dum = pd.get_dummies(data=df,columns = cols_to_transform)
    df_dum = df_dum.fillna(df_dum.mean())
    
    ##############
    
    array = df_dum.values
    train, test = train_test_split(df_dum, test_size = 0.3)
    features = df_dum.columns[1:35]
    seed = 7
    max_features = 3
    #rf = RandomForestClassifier(n_estimators=100, max_features="auto",oob_score = True, 
                               # n_jobs = -1,random_state =50,min_samples_leaf = 50)
    rf = RandomForestClassifier(n_estimators=100, max_features=max_features)
    y, _ = pd.factorize(train['sold_binary'])
    #y = train['sold_binary']
    rf.fit(train[features], y)
    #rf.fit(df_dum,y)
    preds = rf.predict(test[features])
    #preds = rf.predict(df_dum)
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    results = model_selection.cross_val_score(rf, test[features], test['sold_binary'], cv=kfold)
    #print(precision_recall_fscore_support(test['sold_binary'], preds, average='micro'))
    #print(results.mean())
    #print "Features sorted by their score:"
    #print sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), features), 
                 #reverse=True)
    return preds[-1]
