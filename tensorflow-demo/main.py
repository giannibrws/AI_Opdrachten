import tensorflow
import keras
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle


data = pd.read_csv("assets/student-mat.csv", sep=";")


# prints out the head row of dataset:
print(data.head())

# G = grade 1,2,3 etc..
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

# Minimizing our dataset to only 6 parameters:


# print(data.head())

predict = "G3"

# train data without G3
X = np.array(data.drop([predict], 1))
# all G3 values:
y = np.array(data[predict])

print("value of x equals: ", X)
print("value of y equals: ", y)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)


linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)

ac = linear.score(x_test, x_train)

print(ac)
