import sys
import numpy as np
import pandas as pd
import csv
import sklearn
from sklearn import preprocessing
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
from sklearn.model_selection import KFold

f = open(sys.argv[1],'rb')
reader = csv.reader(f)
headers = reader.next() #headers are the plaintext features
df = pd.read_csv(sys.argv[1], sep=',',skiprows=[0],names=headers)
le = preprocessing.LabelEncoder() 
df = df.apply(le.fit_transform) # changes str val in features to ints

#data split
np.random.shuffle(df.values)
all_val = df.drop('sold_binary', axis=1)
all_val = all_val.drop('year_updated', axis=1)
all_val = all_val.drop('lot_size_sq_footage', axis=1)
all_val = all_val.drop('street_address', axis=1)
all_val = all_val.drop('city',axis=1)
all_val = all_val.drop('state',axis=1)
all_val = all_val.drop('zip',axis=1)
all_val = all_val.drop('roof_type',axis=1)
all_label = df[['sold_binary']]

print all_val

observations = len(all_val.index)
trainTestSplit = observations // 3

train_val = all_val.head(observations - trainTestSplit)
train_label = all_label.head(observations - trainTestSplit)
test_val = all_val.tail(trainTestSplit)
test_label = all_label.tail(trainTestSplit)

kf = KFold(n_splits=10, random_state=0)
kf.get_n_splits(all_val)
print kf

rf = RandomForestClassifier(n_estimators=3500,oob_score=True,n_jobs=-1)

rf.fit(train_val.values,train_label.values.ravel())
predicted = rf.predict(test_val.values)



print "Random Forest accuracy score is: " + str(accuracy_score(test_label.values,predicted,normalize='False'))
print str("Out of Bag score is: " + str(rf.oob_score_))
print str("Classification report for classifier %s \n%s\n" % (rf, metrics.classification_report(test_label.values, predicted)))

joblib.dump(rf,'rfTemp.pkl')
