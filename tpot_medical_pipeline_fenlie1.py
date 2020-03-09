import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split

import joblib #jbolib模块

overwrite = False

#   选取前一百个特征 100例AutoML得到的pipeline
# NOTE: Make sure that the outcome column is labeled 'target' in the data file
medical = pd.read_csv('train_fenlie1.csv')
medical = medical.fillna(-999)
medical_new = medical.drop(['ID','Label'], axis=1)

#pd.isnull(medical_new).any()
medical_new = np.array(medical_new.values,dtype=float)
medical_new[np.isnan(medical_new)] = -999

features = medical_new
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, medical['Label'].values , random_state=42)

# Average CV score on the training set was: -15.981117264229795
if overwrite: 
    exported_pipeline = ExtraTreesRegressor(bootstrap=True, max_features=0.5, min_samples_leaf=1, min_samples_split=2, n_estimators=100)
    # Fix random state in exported estimator
    if hasattr(exported_pipeline, 'random_state'):
        setattr(exported_pipeline, 'random_state', 42)
    
    exported_pipeline.fit(training_features, training_target)
    joblib.dump(exported_pipeline, 'Baseline_train_fenlie1_model.pkl')
else:
    exported_pipeline = joblib.load('Baseline_train_fenlie1_model.pkl')
results = exported_pipeline.predict(testing_features)

print(results)
print(testing_target)