#import labs we need:
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from math import sqrt

#read datas from dataset:
dataset = pd.read_csv('https://raw.githubusercontent.com/QueraTeam/college-ml/main/ML_intro/6-%20machine%20learning%20in%20practice/weight_dataset.csv')

dataset['Height']= dataset.Height.apply(lambda val : 2.54*val)
dataset['Weight']= dataset.Weight.apply(lambda val: 0.45359237*val)

#show datas:
dataset.head(10)
dataset.info()
dataset.describe()
sns.scatterplot(x='Height', y='Weight', hue='Gender', data=dataset)
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10000 entries, 0 to 9999
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   Gender  10000 non-null  object 
 1   Height  10000 non-null  float64
 2   Weight  10000 non-null  float64
dtypes: float64(2), object(1)
memory usage: 234.5+ KB

<AxesSubplot:xlabel='Height', ylabel='Weight'>
image...
"""
#change values of gender:
dataset['Gender'].replace('Female',0, inplace=True)
dataset['Gender'].replace('Male',1, inplace=True)


#what?!
x_train,x_test, y_train,y_test = train_test_split(dataset.drop('Weight',axis=1), dataset.Weight, test_size=0.2, random_state=101)
"""
XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
             colsample_bynode=1, colsample_bytree=1, enable_categorical=False,
             gamma=0, gpu_id=-1, importance_type=None,
             interaction_constraints='', learning_rate=0.300000012,
             max_delta_step=0, max_depth=6, min_child_weight=1, missing=nan,
             monotone_constraints='()', n_estimators=100, n_jobs=4,
             num_parallel_tree=1, predictor='auto', random_state=0, reg_alpha=0,
             reg_lambda=1, scale_pos_weight=1, subsample=1, tree_method='exact',
             validate_parameters=1, verbosity=None)
"""
regressor = XGBRegressor(n_estimators=100)
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

print(f'MAE = {mean_absolute_error(y_test,y_pred)}')
#MAE = 3.848802091903812
print(f'XG Boost Regressor is about {round(regressor.score(x_test,y_test)*100)}% accurate!')
#XG Boost Regressor is about 89% accurate!
