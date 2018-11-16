#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:31:42 2018

@author: taylor
"""

import pandas as pd
import matplotlib.pyplot as plot
import math

data = pd.read_csv('index-2.txt', sep = ' ')
x = data['age']
y = data['FEV']
both = pd.DataFrame([x, y], index = ['age', 'FEV'])
both = both.transpose()
both = both[both['FEV']<10]
x = both['age']
y = both['FEV']

'''
plot.plot(x,y, 'ro')
plot.axis([0,max(x),0,max(y)])
plot.show()
'''

def h(x, a, b):
    return a+b*x

def j(a,b):
    total = 0
    for i in range(0, len(x)):
        total += math.pow(h(x[i], a, b) - y[i], 2)
    average = total/len(x)
    cost = average/2
    return cost

def da(a, b):
    total = 0
    for i in range(0, len(x)):
        total += (h(x[i], a, b) - y[i])
    average = total/len(x)
    div = average
    return div

def db(a, b):
    total = 0
    for i in range(0, len(x)):
        total += (h(x[i], a, b) - y[i]) * x[i]
    average = total/len(x)
    div = average
    #print('db: ' + str(div))
    return div

alpha = .016

a = 0
b = 0
i = 0

while (abs(db(a,b)) > .01):
    plot.plot(x,y, 'ro')
    plot.axis([0,max(x)+3,0,max(y)+3])
    xs = [min(x), max(x)]
    ys = [h(min(x), a, b), h(max(x), a, b)]
    #print(ys)
    print('a: ' + str(a) + ',b: ' + str(b))
    plot.plot(xs, ys, 'k-', lw=2)
    plot.show()
    a += -alpha*da(a,b)
    b += -alpha*db(a,b)
    i += 1
   
print('a: ' + str(a) + ',b: ' + str(b))
print('Iterations: ' + str(i))
'''
np.random.seed(5)
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)
plt.plot(x, y, "o")


# draw vertical line from (70,100) to (70, 250)
plt.plot([70, 70], [100, 250], 'k-', lw=2)

# draw diagonal line from (70, 90) to (90, 200)
plt.plot([70, 90], [90, 200], 'k-')

plt.show()



'''
