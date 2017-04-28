# coding: utf-8

# In[ ]:

import mysql.connector
import csv
import pandas as pd
import numpy as np
import scipy
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_fscore_support
import json
#from sklearn.pipeline import Pipeline
#from sklearn.preprocessing import StandardScaler
#from sklearn.preprocessing import Imputer


#zip code for this is 27705
#def sold_classifier(zip_code):
def sold_classifier(zip_code,bedrooms,bathrooms,finished_sq_footage,lot_size_sq_footage,year_built,last_sale_price,home_type,
                   neighborhood,school_district,parking_type,number_of_floors):
    cnx = mysql.connector.connect(user='ctsimaan',password='SeniorProject490',
                              host='nostradomicile-data.c6x7vypetdqh.us-west-2.rds.amazonaws.com',
                              database='PyZillow_Data')
    cursor = cnx.cursor()

###################

    #df_pd = pd.read_sql('SELECT*FROM PyZillow_Data.home_data Where zip = ' + zip_code, con=cnx)
    query = 'SELECT*FROM PyZillow_Data.home_data Where zip =' + zip_code
    df_pd = pd.read_sql(query, con = cnx)
    #pd.set_option('precision',2)
    frames = [df_pd,df_pd]
    df_pd = pd.concat(frames)
    while(len(df_pd)<2000):
        frames = [df_pd,df_pd]
        df_pd = pd.concat(frames)


####################

    new = df_pd.filter(['sold_binary', 'home_type', 'bedrooms', 'bathrooms', 'finished_sq_footage',
       'lot_size_sq_footage','year_built','last_sale_price','neighborhood', 'school_district','parking_type','number_of_floors'], axis = 1)
    df = pd.DataFrame(data = new)
    cols_to_transform = [ 'home_type','neighborhood','school_district','parking_type']
    df_dum = pd.get_dummies(data=df,columns = cols_to_transform)
    df_dum = df_dum.fillna(df_dum.mean())
    
    ##############
    
    array = df_dum.values
    train, test = train_test_split(df_dum, test_size = 0.3)
    d={}
    #d = {'sold_binary':0, 'bedrooms':bedrooms,'bathrooms':bathrooms,'finished_sq_footage':finished_sq_footage,
         #'lot_size_sq_footage':lot_size_sq_footage,'year_built':year_built, 'last_sale_price':last_sale_price,'home_type':home_type,'neighborhood':
         #neighborhood, 'school_district':school_district, 'parking_type':parking_type,'number_of_floors':number_of_floors}
    d['sold_binary']=0
    d['bedrooms']=bedrooms
    d['bathrooms']=bathrooms
    d['finished_sq_footage'] = finished_sq_footage
    d['lot_size_sq_footage'] = lot_size_sq_footage
    d['year_built'] = year_built
    d['last_sale_price'] = last_sale_price
    d['home_type'] = home_type
    d['neighborhood'] = neighborhood
    d['school_district'] = school_district
    d['parking_type'] = parking_type
    d['number_of_floors'] = number_of_floors
    
    dic_str = ""
    for key,val in d.iteritems():
      dic_str = dic_str + key + str(val)

    
    #rowCount = len(df_dum.index)
    #d = pd.DataFrame(data = d, index=[rowCount])
    #cols_to_transform = [ 'home_type','neighborhood','school_district','parking_type']
    #d = pd.get_dummies(data=d,columns = cols_to_transform)
    #addData = [test,d]
    #test = pd.concat(addData)
    #test = test.fillna(test.mean())
    colCount = len(df_dum.columns)
    features = df_dum.columns[1:colCount]

    
    seed = 7
    max_features = 3
    #rf = RandomForestClassifier(n_estimators=100, max_features="auto",oob_score = True, 
                                #n_jobs = -1,random_state =50)
    rf = RandomForestClassifier(n_estimators=100, max_features=max_features)
    
    y, _ = pd.factorize(train['sold_binary'])
    #y = train['sold_binary']
    #train = Imputer().fit_transform(train[features])
    #rf.fit(train, y)
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
    #result = json.dumps(preds[-1])
    #result = json.loads(preds[-1])
    preds = np.array(map(str, preds))
    #preds[-1]
    return dic_str[-1]
