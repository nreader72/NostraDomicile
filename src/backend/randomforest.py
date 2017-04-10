import mysql.connector 
import sqlite3
import pandas as pd
from sklearn import svm, metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import KFold
from sklearn import metrics
import joblib
import numpy as np
import random
import time
from sklearn import preprocessing
#def to_csv():
#    db = mysql.connector.connect(user='oemarsha',password='SeniorProject490',host='http://nostradomicile-data.c6x7vypetdgh.us-west-2.rds.amazonaws.com/',database='PyZillow_Data')
#    cursor = db.cursor()
#    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#    tables = cursor.fetchall()
#    for table_name in tables:
#        table_name = table_name[0]
#        table = pd.read_sql_query("SELECT * from %s" % table_name, db)
#        table.to_csv(table_name + '.csv', index_label='index')
dataset = pd.read_csv('28205.csv')
print "Random Forest is loading..."
all_data = dataset.as_matrix
print(all_data)



le = preprocessing.LabelEncoder()
#n_samples = len(all_data)
#le.fit(all_data)

X = []
y = []
for value,label in all_data:
	X.append(value)
	y.append(label)
X = np.array(X)
y = np.array(y)

le.fit(y)
np.random.shuffle(all_data)
kf = KFold(n_samples, n_folds=10)
k = 0
start_time = time.time()


for train, test in kf:
    rfc = RandomForestClassifier(n_estimators=100)	
    rfc.fit(X[train], y[train])
    predicted = rfc.predict(X[train])
    file.write(str(rfc.score(X[test],y[test])))
    file.write(str("\n"))
   
print "Random Forest complete"
