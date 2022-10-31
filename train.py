# load required packages
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer # for one-hot encoding
from sklearn.ensemble import RandomForestClassifier
import bentoml

# load and prep data
df = pd.read_csv('train.csv').drop(columns='id')

df_train_full, df_test = train_test_split(df, train_size = 0.8, test_size = 0.2, random_state=30)
df_train, df_valid = train_test_split(df_train_full, train_size = 0.75, test_size = 0.25, random_state=11)

y_train = df_train.Response#.values

categorical = ['Gender', 'Driving_License', 'Region_Code',
               'Previously_Insured', 'Vehicle_Age', 'Vehicle_Damage',
               'Policy_Sales_Channel']

X_train = df_train.drop(columns='Response')

# dict transformation of categorical variables
train_dict = X_train[categorical].to_dict(orient='records')
dv = DictVectorizer(sparse=False) # initialize DictVectorizer on df that contains all relevant information
X_train = dv.fit_transform(train_dict)

# train final model
rf = RandomForestClassifier(n_estimators = 50,
                            max_depth = 10,
                            random_state = 1, 
                            n_jobs = -1)
rf.fit(X_train, y_train)

# + saving final model to file using pickle or bentoml
saved_model = bentoml.sklearn.save_model("insurance_response", 
                                         rf,
                                         custom_objects = {"dictVectorizer": dv},
                                         signatures = {"predict_proba": {"batchable": False}}
                                        )
print(f"Model saved: {saved_model}")