from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

np.random.seed(0)

iris = load_iris()
df = pd.DataFrame(iris.data, columns= iris.feature_names)
print(df.head())

df['species'] = pd.Categorical.from_codes(iris.target,iris.target_names)

print("Species:\n", df.head())

df['is_train'] = np.random.uniform(0,1,len(df)) >= .75

print("Is train:\n", df.head())

train, test = df[df['is_train']==True], df[df['is_train']==False]

print('Number of Training Data points:', len(train))
print('Number of Test Data points:', len(test))

features = df.columns[:4]

print(features)

y = pd.factorize(train['species'])[0]
print(y)

clf = RandomForestClassifier(n_jobs=2,random_state=0)

clf.fit(train[features],y)

RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini', 
                       max_depth=None, max_features='auto', max_leaf_nodes=None, 
                       min_samples_leaf=1,
                       min_samples_split=2, min_weight_fraction_leaf=0.0,
                       n_estimators=10, n_jobs=2, oob_score=False, random_state=0,
                       verbose=0, warm_start=False)

preds = clf.predict(test[features])

print(pd.crosstab(test['species'], preds, rownames = ['Actual Species'], colnames=['Predicted Species']))

print(list(zip(train[features],clf.feature_importances_)))