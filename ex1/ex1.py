import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from funtions_to_implement import warm_up_exercise
from funtions_to_implement import plot_data
from funtions_to_implement import compute_cost
from funtions_to_implement import gradient_descent

## Machine Learning Online Class - Exercise 1: Linear Regression

#  Instructions
#  ------------
#
#  This file contains code that helps you get started on the
#  linear exercise. You will need to complete the following functions
#  in this exericse:
#
#     funtions_to_implement.py
#     plot_data.py
#     gradient_descent.py
#     compute_cost.py
#     gradient_descent_multi.py
#     compute_cost_multi.py
#     feature_normalize.py
#     normal_eqn.py
#
#  For this exercise, you will not need to change any code in this file,
#  or any other files other than those mentioned above.
#
# x refers to the population size in 10,000s
# y refers to the profit in $10,000s
#

## ==================== Part 1: Basic Function ====================
# Note: You have to complete the code in funtions_to_implement.py

print('Running warmUpExercise ... \n')
print('5x5 Identity Matrix: \n')
warm_up_exercise()

print('Program paused. Press enter to continue.\n')
input()

## ======================= Part 2: Plotting =======================
print('Plotting Data ...\n')
data = pd.read_csv('ex1data1.txt', header=None)
X = data.iloc[:, 0]
y = data.iloc[:, 1]
m = y.size # number of training examples

# Plot Data
# Note: You have to complete the code in funtions_to_implement.py
plot_data(X, y);

print('Program paused. Press enter to continue.\n');
input()

## ================== Part 3: Gradient descent ====================
print('Running Gradient Descent ...\n')

X = np.column_stack((np.ones(m), data.values[:,1])) # Add a column of ones to x
theta = np.zeros((2,1)) # initialize fitting parameters

# Some gradient descent settings
iterations = 1500
alpha = 0.01

# compute and display initial cost
compute_cost(X, y, theta)

# run gradient descent
theta = gradient_descent(X, y, theta, alpha, iterations)[0]

# print theta to screen
print('Theta found by gradient descent: ', theta, '\n')

# Plot the linear fit
figure = plt.figure()
ax = figure.add_subplot(111)
ax.plot(X[:,1], np.matmul(X, theta), linewidth=3)
ax.set(title='An Example Axes', xlabel='Training data', ylabel='Linear regression')
plt.show()

# Predict values for population sizes of 35,000 and 70,000
predict1 = theta * [1, 3.5]
print('For population = 35,000, we predict a profit of ', predict1*10000, '\n')
predict2 = [1, 7] * theta
print('For population = 70,000, we predict a profit of ', predict2*10000, '\n')

print('Program paused. Press enter to continue.\n')
input()