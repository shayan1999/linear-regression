import numpy as np

def cost_function( x, y, theta0, theta1 ):
    """Compute the squared error cost function

    Inputs:
    x        vector of length m containing x values
    y        vector of length m containing y values
    theta_0  (scalar) intercept parameter
    theta_1  (scalar) slope parameter

    Returns:
    cost     (scalar) the cost
    """

    cost = 0.0

    ##################################################
    h0 = theta0 + (np.array(x) * theta1)
    e = h0 - np.array(y)
    cost = np.sum(e ** 2) / 2

    # how it works::
    # as you said I didn't use loops for this question
    # I used vectors operations which numpy gives us
    # first I calculate h0 as you provided in the question
    # after that I calculated the error part h0(xi)-yi
    # and finally I use sum from numpy to calculate sum of all
    # our errors^2 and after that divide them by two
    # this version is much faster than using for loop  
    ##################################################
    
    return cost


def gradient(x, y, theta_0, theta_1):
    """Compute the partial derivative of the squared error cost function

    Inputs:
    x          vector of length m containing x values
    y          vector of length m containing y values
    theta_0    (scalar) intercept parameter
    theta_1    (scalar) slope parameter

    Returns:
    d_theta_0  (scalar) Partial derivative of cost function wrt theta_0
    d_theta_1  (scalar) Partial derivative of cost function wrt theta_1
    """
    d_theta_0, d_theta_1 = 0, 0
    ##################################################
    h = theta_0 + theta_1 * x
    d_theta_0 = np.sum(h - y) 
    d_theta_1 = np.sum((h - y) * x)

    # I mentioned the formulas I used here in our notebook
    # so after you see those formula this snippet will be 
    # so clear for you I used basic numpy vectors operations
    # to create those formula I used np.sum for sigma and rest of 
    # it is basic mathematic symbols
    ##################################################

    return d_theta_0, d_theta_1 # return is a tuple

def explicit_answer(x, y):
    """Compute the explicit values of theta1 and theta2

    Inputs:
    x          vector of length m containing x values
    y          vector of length m containing y values

    Returns:
    theta_0  (scalar) intercept of line
    theta_1  (scalar) slope of line
    """
    
    
    ##################################################
    # TODO: write code here to compute explicit values of theta_0 and theta_1
    # Convert x and y to numpy arrays if they aren't already
    x = np.array(x)
    y = np.array(y)

    # Calculate means of x and y
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # Calculate theta_1
    numerator = np.sum((x - mean_x) * (y - mean_y))
    denominator = np.sum((x - mean_x) ** 2)
    ex_theta_1 = numerator / denominator

    # Calculate theta_0
    ex_theta_0 = mean_y - ex_theta_1 * mean_x
    
    return ex_theta_0, ex_theta_1
    ##################################################