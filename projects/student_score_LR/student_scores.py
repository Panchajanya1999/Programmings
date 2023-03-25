# ML code to predict the percentage of marks that a student is expected to score based upon the number of hours they studied. This is a simple linear regression task as it involves just 2 variables.

import pandas as pd
import numpy as np  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn import metrics

# read the data
df = pd.read_csv("student_scores.csv")

# Assign X and y
X = df.iloc[:, 0].values
y = df.iloc[:, 1].values

# Reshape X and y
X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.85, random_state=1)

# Create the model
regressor = LinearRegression()

# Fit the model
regressor.fit(X_train, y_train)

# create a function so that the result does not go beyond 100
def check_res(res):
    if res >= 100:
        return 100
    else:
        return res

# predict the score if the student studies for certain hours a day which is taken as input from the user
hours = float(input("Enter the number of hours the student studies: "))
print("The predicted score of the student is:", check_res(int(round(regressor.predict([[hours]])[0][0], 0))))