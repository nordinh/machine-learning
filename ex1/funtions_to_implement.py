import numpy as np

# WARMUPEXERCISE Example function
#   A = WARMUPEXERCISE() is an example function that returns the 5x5 identity matrix

# ============= YOUR CODE HERE ==============
# Instructions: Return the 5x5 identity matrix
#
def warm_up_exercise():
    return

# PLOTDATA Plots the data points x and y into a new figure
#   PLOTDATA(x,y) plots the data points and gives the figure axes labels of
#   population and profit.

# ====================== YOUR CODE HERE ======================
# Instructions: Plot the training data into a figure using the
#               "figure" and "plot" commands. Set the axes labels using
#               the "xlabel" and "ylabel" commands. Assume the
#               population and revenue data have been passed in
#               as the x and y arguments of this function.
#
# Hint: You can use the 'rx' option with plot to have the markers
#       appear as red crosses. Furthermore, you can make the
#       markers larger by using plot(..., 'rx', 'MarkerSize', 10);
def plot_data(x, y):
    return

# COMPUTECOST Compute cost for linear regression
#   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
#   parameter for linear regression to fit the data points in X and y
#
def compute_cost(X, y, theta):
    m = y.size     # number of training examples

    # You need to return the following variables correctly
    J = 0;

    # ====================== YOUR CODE HERE ======================
    # Instructions: Compute the cost of a particular choice of theta
    #               You should set J to the cost.

    # for i=1:size(X, 1);
    #   J = J + (1 / (2 * m) * (X(i,:)*theta - y(i))^2);
    # end;



    # =========================================================================
    return J

# GRADIENTDESCENT Performs gradient descent to learn theta
#   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by
#   taking num_iters gradient steps with learning rate alpha
def gradient_descent(X, y, theta, alpha, num_iters):
    # Initialize some useful values
    m = y.size    # number of training examples
    J_history = np.zeros((num_iters, 1))
    for iter in range(num_iters):
        # ====================== YOUR CODE HERE =======================
        # Instructions: Perform a single gradient step on the parameter vector
        # theta.
        #
        # Hint: While debugging, it can be useful to print out the values
        # of the cost function(computeCost) and gradient here.
        #


        # for i=1:size(X, 2)
        #   theta(i) = theta(i) - alpha/m*(X(:,i)'*delta);
        # end;


        # ============================================================

        # Save the cost J in every iteration
        J_history[iter] = compute_cost(X, y, theta)

    return theta, J_history
