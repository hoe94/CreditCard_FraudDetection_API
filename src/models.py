import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV


from imblearn.combine import SMOTETomek
import xgboost as xgb
import pickle

from downcast import downcast
pd.set_option('display.max_columns', None)


df = pd.read_csv('data\train.csv')
df = downcast(df)

'''1. Impute the missing values'''
for i in df.columns:
    df[i] = np.where(df[i].isnull(), df[i].mean(), df[i])

'''2. Apply the Smotetomek on Imbalanced data'''
df_X = df.iloc[:,:27]
df_Y = df['Class']
osus = SMOTETomek(random_state = 42)
df_X_osus, df_Y_osus = osus.fit_resample(df_X, df_Y)

'''3. Standardize all the input feature value range'''
scaler = StandardScaler()
amount = df_X_osus['Amount']
transform_amount = scaler.fit_transform(amount.values.reshape(-1,1))
df_X_osus.drop('Amount', axis = 1, inplace = True)
df_X_osus['Amount'] = transform_amount

'''4. Fit & Train the data into the XgBoost Model'''
df_train_X, df_test_X, df_train_Y, df_test_Y = train_test_split(df_X_osus, df_Y_osus, test_size = 0.4)
xgboost_classifier = xgb.XGBClassifier(learning_rate= 0.4, max_depth = 4, min_child_weight = 2, n_estimators =  500, gamma = 0.05)
xgboost_classifier.fit(df_train_X, df_train_Y)
with open('models\model.pkl', 'wb')as f:
  pickle.dump(xgboost_classifier, f)