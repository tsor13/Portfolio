import pandas as pd
import matplotlib.pyplot as plot
import math
import numpy as np

alpha = .1
'''
data = pd.read_csv('Data/cancer.csv')
y = data['diagnosis']
cols_interest = ['perimeter_mean','radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean']
X = data[cols_interest]
#Replace text output with int
y = y.replace({'M':1, 'B':0})
#Normalize the data
X = (X-X.min())/(X.max()-X.min()-.5)*10
#initialize theta to random numbers
theta = (pd.DataFrame(np.random.rand(len(X.columns), 1))-.5)

'''
data = pd.read_csv('Data/test.csv')
y = data['Classification']
cols_interest = ['Length', 'Weight']#['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean']
X = data[cols_interest]
#Normalize the data
X = ((X-X.min())/(X.max()-X.min())-.5)*10
#initialize theta to random numbers
theta = (pd.DataFrame(np.random.rand(len(X.columns), 1))-.5)

#hypothesis given input
def h_1(i):
    return 1/(1+math.exp(-i))

def h(x, params):
    v = np.dot(x, params)
    df = pd.DataFrame(v)
    df = df.apply(lambda row: h_1(row[0]), axis = 1)
    return df

#cost function
def j():
    total = 0
    for i in range(0, len(X)):
        h = h_1(np.dot(X.iloc[i], theta)[0])
        if(y[i] == 1):
            total += math.log(h)
        else:
            total += math.log(1-h)
    cost = -total/len(X)
    return cost

#derivative function
def dj(j):
    total = 0
    for i in range(0, len(X)):
        h = h_1(np.dot(X.iloc[i], theta)[0])
        total += (h-y[i])*X.iloc[i, j]
    cost = total/len(X)
    return cost

def dtheta(t, a):
    dtheta = t.copy()
    for i in range(0, len(t)):
        dtheta[0][i] = a*dj(i)
        #print(dtheta[0, i])
    return dtheta
    
cost = 1
dt = dtheta(theta, alpha)
iter = 0
while(abs(dt.sum()[0]) > .00005):
    cost = j()
    dt = dtheta(theta, alpha)
    theta = theta - dt
    print('Dtheta:', dt)
    print('Theta: ', theta, 'Cost: ', cost)
    iter+=1
print("Iterations: ", iter)
y_pred = h(X, theta)
