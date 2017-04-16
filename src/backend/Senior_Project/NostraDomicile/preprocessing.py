from sklearn import preprocessing
import pandas as pd
le = preprocessing.LabelEncoder()
file_df = pd.read_csv("Zip_Zhvi_Summary_AllHomes.csv")
arr = file_df.as_matrix()
le.fit(arr)
le.transform(arr)

