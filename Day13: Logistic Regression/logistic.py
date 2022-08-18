"""
This code assumes you have read the Logistic Regression Blog Post
If not, then read the complete article to understand the code
https://animevyuh.org/logistic-regression/
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class StandardScalar():
    def fit_transform(self,x):
        mean = np.mean(x,axis=0)
        std_dev = np.std(x)
        return (x-mean)/std_dev


# read the dataset
train_data = pd.read_csv("hr_job.csv")
train_data.fillna(method="bfill",inplace=True)

train_data.drop('city',axis=1,inplace=True)
X = train_data.iloc[:,:-1]
Y = train_data.target

#scale the dataset
sc = StandardScalar()
X = sc.fit_transform(X)


def initialize_weights(dim):
    W = np.full((dim,1),0.1)
    b = 0.0
    return W,b
    
def activation(Z):
    sigmoid = 1/(1+np.exp(-Z))
    return sigmoid

def costFunction(y_pred,y):
    training_samples = y.shape[0]
    loss = (y*np.log(y_pred))+((1-y)*np.log(1-y_pred))
    return -np.sum(loss)/training_samples

def gradient_descent(x_train,y_train,y_pred):
    cost = costFunction(y_pred,y_train)
    derivative_weight = (np.dot(x_train.T,(y_pred-y_train)))/x_train.shape[0] 
    derivative_bias = np.sum(y_pred-y_train,keepdims=True)/x_train.shape[0]
    gradients = {"dW": derivative_weight,"db": derivative_bias}
    return cost,gradients

def update(W,b,x_train,y_train,y_pred,learning_rate,number_of_iterations):
    costRecord = []
    for i in range(number_of_iterations):
        cost,gradients = gradient_descent(x_train,y_train,y_pred)
        W -= learning_rate*gradients['dW']
        b -= learning_rate*gradients['db']
        if i%100 == 0:
            costRecord.append(cost)
    parameters = {'W':W,'b':b}
    plt.plot(costRecord,np.arange(0,number_of_iterations,100))
    plt.show()
    return parameters

def predict(W,b,x):
    Y_prediction = np.zeros((x.shape[0],1))
    z = np.dot(X,W)+b
    y_pred = activation(z)
    print(y_pred.shape[0])
    for i in range(y_pred.shape[1]):
        if y_pred[i,0]< 0.5:
            Y_prediction[i,0] = 0
        else:
            Y_prediction[i,0] = 1
    return Y_prediction

Y = Y.to_numpy().reshape(-1,1)
x_T,x_V,y_T,y_V = train_test_split(X,Y,train_size=0.75)

def logistic_regression(x_train, y_train,x_test,y_test,learning_rate ,  num_iterations):
    W,b = initialize_weights(x_train.shape[1])
    z = np.dot(x_train,W)+b
    y_pred = activation(z)
    parameters = update(W, b, x_train, y_train,y_pred,learning_rate,num_iterations)

    y_prediction_train = predict(parameters['W'],parameters['b'],x_train)
    y_prediction_test = predict(parameters['W'],parameters['b'],x_test)

    print("Train accuracy: {} %".format(100 - np.mean(np.abs(y_prediction_train - y_train)) * 100))
    print("Test accuracy: {} %".format(100 - np.mean(np.abs(y_prediction_test - y_test)) * 100))
    
logistic_regression(x_T,y_T,x_V,y_V,0.001 , 1000)

#from sklearn

model = LogisticRegression()
model = model.fit(x_T,y_T)
predict = model.predict(x_V)

print(model.score(x_T,y_T))
from sklearn.metrics import accuracy_score
print(accuracy_score(y_pred=predict,y_true=y_V))

#the reason why we are getting more accuracy in trained sklearn model ,because we didn't perform Regularization manuall
