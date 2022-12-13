#!/bin/python

# import libraries
import numpy as np 
import pandas as pd 
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_curve, auc, roc_curve

# ignore warnings
import warnings
warnings.filterwarnings('ignore')

# read the data rom a csv file
df = pd.read_csv('datasets/mushrooms.csv')

'''
# uncomment the following code to download the dataset from the internet
dset = ''
url = ''
# check if the datset exists and if it does not, download the dataset from the internet
if not os.path.exists(dset):
    df = pd.read_csv(url)
'''

# we will convert the ordinal data to categorical data
df = df.astype('category')

# use LabelEncoder to convert the categorical data to numerical data
le = LabelEncoder()
df = df.apply(le.fit_transform)

# check the column with all-zero datasets and drop them
df = df.loc[:, (df != 0).any(axis=0)]

# drop class column from the data
X = df.drop(['class'], axis=1)

# assign the class column to y
y = df['class']

# perform PCA to reduce dimensions of dats
from sklearn.decomposition import PCA
pca = PCA(n_components = 7, svd_solver = 'full', whiten = True)
X = pca.fit_transform(X)

# split the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=123)

# check scores of Classification models

# import lazypredict library 
from lazypredict.Supervised import LazyClassifier

# define the lazypredict classifier with the parameters
clf = LazyClassifier(verbose=0, ignore_warnings=True, custom_metric=None)
models, predictions = clf.fit(X_train, X_test, y_train, y_test)

# print the models and their scores
print(models)

# create  function to check the accuracy of agiven array and return the accuracy in percentage
def check_accuracy(y_test, y_pred):
    correct = 0
    for i in range(0, len(y_test)):
        if y_test[i] == y_pred[i]:
            correct += 1
    return round((correct/len(y_test))*100, 3)

# implement Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier

# implement Random Forest Classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1, bootstrap=True)
rf.fit(X_train, y_train)

# predict the dataset
preds = rf.predict(X_test)
print(f"The accuracy of the prdicted dataset with the actual dataset is {check_accuracy(preds, y_test.values)}%")
