def classify(input_csv):
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

	f = open(input_csv,'rb')
	reader = csv.reader(f)
	headers = reader.next() #headers are the plaintext features
	df = pd.read_csv(input_csv, sep=',',skiprows=[0],names=headers)
	le = preprocessing.LabelEncoder() 
	df = df.apply(le.fit_transform) # changes str val in features to ints

	#data split
	np.random.shuffle(df.values)
	all_val = df.drop('sold_binary', axis=1)
	all_label = df[['sold_binary']]


	rf = joblib.load('rfTemp.pkl')
	predicted = rf.predict(all_val.values)

	return "Random Forest accuracy score is: " + str(accuracy_score(all_label.values,predicted,normalize='False')) +  str("Out of Bag score is: " + str(rf.oob_score_)) + str("Classification report for classifier %s \n%s\n" % (rf, metrics.classification_report(all_label.values, predicted)))

def prediction(userDict):
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
	from sklearn.feature_selection import SelectFromModel

	userdf = pd.DataFrame(userDict, index=[0])
	userdf = userdf.drop('sold_binary',axis=1)
	print userdf
	rf = joblib.load('rfTemp.pkl')
	le = preprocessing.LabelEncoder()
	userdf = userdf.apply(le.fit_transform) #
	prediction = rf.predict(userdf)

	return prediction

def feat_extract(input_csv):
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
        from sklearn.feature_selection import SelectFromModel
	
	f = open(input_csv,'rb')
        reader = csv.reader(f)
        headers = reader.next() #headers are the plaintext features
        df = pd.read_csv(input_csv, sep=',',skiprows=[0],names=headers)
        le = preprocessing.LabelEncoder()
        df = df.apply(le.fit_transform) # changes str val in features to ints

        #data split
        np.random.shuffle(df.values)
        all_val = df.drop('sold_binary', axis=1)
        all_val = df.drop('sold_binary', axis=1)
	all_val = all_val.drop('year_updated', axis=1)
	all_val = all_val.drop('lot_size_sq_footage', axis=1)
	all_val = all_val.drop('street_address', axis=1)
	all_val = all_val.drop('city',axis=1)
	all_val = all_val.drop('state',axis=1)
	all_val = all_val.drop('zip',axis=1)
	all_val = all_val.drop('roof_type',axis=1)
	all_label = df[['sold_binary']]

	features = []
        rf = joblib.load('rfTemp.pkl')
        predicted = rf.predict(all_val.values)
	sfm = SelectFromModel(rf, threshold=0.15)
        sfm.fit(all_val, all_label)
	for feature_list_index in sfm.get_support(indices=True):
		print(headers[feature_list_index])
		features.append(headers[feature_list_index])

	return features
