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

def to_csv():
    db = mysql.connector.connect(user='oemarsha',password='SeniorProject490',host='http://nostradomicile-data.c6x7vypetdgh.us-west-2.rds.amazonaws.com/',database='PyZillow_Data')
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table_name in tables:
        table_name = table_name[0]
        table = pd.read_sql_query("SELECT * from %s" % table_name, db)
        table.to_csv(table_name + '.csv', index_label='index')



dataset = open('PyZillow_Data.csv','rb') 
print "Random Forest is loading..."
all_data = open(dataset,"r")
#file= open('randomforest_experiment.txt','w')
random.shuffle(all_data)
n_samples = len(all_data)
X = []
y = []
for value,label in all_data:
	X.append(value)
	y.append(label)
X = np.array(X)
y = np.array(y)
kf = KFold(n_samples, n_folds=10)
k = 0
start_time = time.time()

for train, test in kf:
    rfc = RandomForestClassifier(n_estimators=100)	
    rfc.fit(X[train], y[train])
    predicted = rfc.predict(X[train])
    if (kf == 10):
	start_time = time.time() # doesn't work because scoping
   # file.write(str("Classification report for classifier %s \n%s\n" % (rfc, metrics.classification_report(y[test], predicted))))
    file.write(str(rfc.score(X[test],y[test])))
    file.write(str("\n"))
    k+=1

#file.write(str("Time it took to execute: " + str(time.time() - start_time) + " seconds."))    
print "Random Forest complete"
pack = joblib.dump(rfc, 'forest.pkl')

#file.close
