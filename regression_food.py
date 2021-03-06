# -*- coding: utf-8 -*-
"""Regression_Food.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jvPMDMtRVR6keoYovMijvRGmSbJ2AFW8
"""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

df = pd.read_csv('/content/train.csv')
test = pd.read_csv('/content/test_QoiMO9B.csv')
df.head()
df.describe()

fulfilment_center = pd.read_csv('/content/fulfilment_center_info.csv')
fulfilment_center.head()

df_center_data = pd.merge(df, fulfilment_center,on='center_id')
test_center = pd.merge(test, fulfilment_center,on='center_id')
test_center.head()
test_center.count()

meal_info = pd.read_csv('/content/meal_info.csv')
meal_info.head()

df_final = pd.merge(df_center_data, meal_info,on='meal_id')
test_final = pd.merge(test_center, meal_info,on='meal_id')

df_final.head()

columns_to_drop = ['center_id', 'meal_id']
df_final.drop(labels=columns_to_drop,axis=1,inplace=True)
test_final.drop(labels=columns_to_drop,axis=1,inplace=True)
df_final.head()

df_final.dtypes

df_final_dummies=pd.get_dummies(df_final)
test_final_dummies=pd.get_dummies(test_final)
test_final_dummies.T.head(31)

y=df_final_dummies['num_orders']
X=df_final_dummies.drop(['num_orders'],axis=1)
X_test=test_final_dummies
display(X.head())
X_test.head()

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(16, 12))
sns.heatmap(X.corr())

Pred_id=X_test.id
columns_to_drop=['base_price','id']
X.drop(['base_price'],axis=1,inplace=True)
X_test.drop(['base_price'],axis=1,inplace=True)



from sklearn.ensemble import RandomForestRegressor
mm=RandomForestRegressor(n_jobs=-1,n_estimators=200,oob_score=True)

from google.colab import drive
drive.mount('/content/drive')

mm.fit(X.values,np.array(y))

y_preds=mm.predict(X_test.values)
np.sum(y_preds<0)

submission=pd.read_csv("/content/sample_submission_hSlSoT6.csv")
submission.head()
submission['id']=Pred_id