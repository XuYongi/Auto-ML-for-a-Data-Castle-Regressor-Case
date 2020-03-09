# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:40:59 2020

@author: Admin
"""

import numpy as np
import pandas as pd


import joblib #jbolib模块




# NOTE: Make sure that the outcome column is labeled 'target' in the data file
medical = pd.read_csv('test.csv')
medical = medical.fillna(-999)
medical_new = medical.drop(['ID'], axis=1)

#pd.isnull(medical_new).any()
medical_new = np.array(medical_new.values,dtype=float)
medical_new[np.isnan(medical_new)] = -999

features = medical_new
#training_features, testing_features, training_target, testing_target = \
#            train_test_split(features, medical['Label'].values , random_state=42)


exported_pipeline = joblib.load('Baseline_train_fenlie1_model.pkl')
results = exported_pipeline.predict(features)


medical.insert(29,'Label',results)
medical.to_csv('upload.csv',index = 0)
#再用excel删除多余列更快捷

print(medical['Label'].values)
