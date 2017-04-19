
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
import matplotlib.pyplot as plt

def attribute_classifier(zip_code)
    cnx = mysql.connector.connect(user='ctsimaan',password='SeniorProject490',
                              host='nostradomicile-data.c6x7vypetdqh.us-west-2.rds.amazonaws.com',
                              database='PyZillow_Data')
    cursor = cnx.cursor()


# In[2]:

df_pd = pd.read_sql('SELECT*FROM PyZillow_Data.home_data Where zip = 27705', con=cnx)
#print(df_pd)
frames = [df_pd,df_pd]
df_pd = pd.concat(frames)
#list(df_pd)


# In[3]:

#new = df_pd.filter(['sold_binary', 'home_type', 'bedrooms', 'bathrooms', 'finished_sq_footage',
       #'lot_size_sq_footage','year_built','last_sale_price','neighborhood', 'school_district'], axis = 1)
    df_pd.drop(['street_address','zip','city', 'state','room_types','roof_type','last_sold_date','heating_system'],inplace=True,axis=1)
    cols_to_transform = [ 'home_type','neighborhood','school_district','appliances','floor_covering','heating_sources','parking_type']
    df_dum = pd.get_dummies(data=df_pd,columns = cols_to_transform)
    df_dum = df_dum.fillna(df_dum.mean())


# In[4]:

train, test = train_test_split(df_dum, test_size = 0.2)
#how to fix sold binary showing up in wrong position
bSoldDF = pd.DataFrame(df_dum.pop('sold_binary'))
#dfs= [bSoldDF,df_dum]
df_dum = pd.concat([bSoldDF,df_dum],axis=1)
col_length = len(df_dum.columns)
#have to get the length of df_dum before this
features = df_dum.columns[1:col_length]
#df_dum =df_dum.reindex(columns=['sold_binary'],cols[-1:].union(cols[:-1]) )
#df_dum.insert('bedrooms', 'sold_binary', df_dum.mean(1))
#print(features)


# In[5]:

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
#print sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), features), 
         #reverse=True)
#print(rf.feature_importances_)


# In[6]:

# make importances relative to max importance
    feature_importance = 100.0 * (feature_importance / feature_importance.max())
 
# A threshold below which to drop features from the final data set. Specifically, this number represents
# the percentage of the most important feature's importance value
    fi_threshold = 15
 
# Get the indexes of all features over the importance threshold
    important_idx = np.where(feature_importance > fi_threshold)[0]
 
# Create a list of all the feature names above the importance threshold
    important_features = features[important_idx]
    #print(important_features)
#print("n", important_features.shape[0], "Important features(>", fi_threshold, "% of max importance):n",important_features)
    return important_features
# Get the sorted indexes of important features
#sorted_idx = np.argsort(feature_importance[important_idx])[::-1]
#print("nFeatures sorted by importance (DESC):n", important_features[sorted_idx])
 
# Adapted from http://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html
#pos = np.arange(sorted_idx.shape[0]) + .5
#plt.subplot(1, 2, 2)
#plt.barh(pos, feature_importance[important_idx][sorted_idx[::-1]], align='center')
#plt.yticks(pos, important_features[sorted_idx[::-1]])
#plt.xlabel('Relative Importance')
#plt.title('Variable Importance')
#plt.draw()
#plt.show()
 
# Remove non-important features from the feature set, and reorder those remaining
#X = X[:, important_idx][:, sorted_idx]


# In[ ]:




# In[ ]:



