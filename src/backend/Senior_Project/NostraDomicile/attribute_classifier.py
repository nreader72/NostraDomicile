
# coding: utf-8

# In[1]:

import mysql
import mysql.connector
import csv
import pandas as pd
import numpy as np
import scipy
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_fscore_support
#import matplotlib.pyplot as plt

def attribute_classifier(zip_code):
    cnx = mysql.connector.connect(user='ctsimaan',password='SeniorProject490',
        host='nostradomicile-data.c6x7vypetdqh.us-west-2.rds.amazonaws.com',
        database='PyZillow_Data')
    cursor = cnx.cursor()


    # In[2]:

    query = 'SELECT*FROM PyZillow_Data.home_data Where zip =' + zip_code
    df_pd = pd.read_sql(query, con = cnx)
    #print(df_pd)
    frames = [df_pd,df_pd]
    df_pd = pd.concat(frames)
    #list(df_pd)


    # In[3]:

    
    df_pd.drop(['street_address','zip','city', 'state','room_types','roof_type','last_sold_date','heating_system'],inplace=True,axis=1)
    cols_to_transform = [ 'home_type','neighborhood','school_district','appliances','floor_covering','heating_sources','parking_type']
    df_dum = pd.get_dummies(data=df_pd,columns = cols_to_transform)
    df_dum = df_dum.fillna(df_dum.mean())


    # In[4]:

    train, test = train_test_split(df_dum, test_size = 0.2)
    #how to fix sold binary showing up in wrong position
    bSoldDF = pd.DataFrame(df_dum.pop('sold_binary'))
    df_dum = pd.concat([bSoldDF,df_dum],axis=1)
    col_length = len(df_dum.columns)
    #have to get the length of df_dum before this
    features = df_dum.columns[1:col_length]
    

    seed = 7
    max_features = 3
    #rf = RandomForestClassifier(n_estimators=100, max_features="auto",oob_score = True, 
                        #n_jobs = -1,random_state =50,min_samples_leaf = 50)
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
    feature_importance = rf.feature_importances_
    #print "Features sorted by their score:"
    

    # In[6]:

    # make importances relative to max importance
    feature_importance = 100.0 * (feature_importance / feature_importance.max())
 
    # A threshold below which to drop features from the final data set. Specifically, this number represents
    # the percentage of the most important feature's importance value
    # @ctsimaan - increased fi_threshold to 50 from 15 in order to reduce list of output attributes.
    fi_threshold = 30
    # Get the indexes of all features over the importance threshold
    important_idx = np.where(feature_importance > fi_threshold)[0]
    # Create a list of all the feature names above the importance threshold
    important_features = features[important_idx]
    # Get the sorted indexes of important features
    sorted_idx = np.argsort(feature_importance[important_idx])[::-1]
    pos = np.arange(sorted_idx.shape[0]) + .5
    fiKeys = important_features[sorted_idx]
    fiValues = feature_importance[important_idx][sorted_idx[::1]]
    #importance = pd.DataFrame(data =fiKeys , index=sorted_idx[::1],columns=["Features"])
    #test = pd.DataFrame(data=fiValues, index=sorted_idx[::1],columns=["Importance"])
    #feat_rank = pd.concat([importance,test],axis=1)
    feat_rank = []
    for x in range(len(fiKeys)):
        feat_rank.append(fiKeys[x])
        feat_rank.append(",")
        feat_rank.append(fiValues[x])
        feat_rank.append(",")

    feat_rank = ''.join(str(e) for e in feat_rank)        
    #print(important_features)
    #print("n", important_features.shape[0], "Important features(>", fi_threshold, "% of max importance):n",important_features)
    #return important_features
    return feat_rank


