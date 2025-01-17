# Root Finding Method
import math
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


def plot_function(func, a, b):
    """
    This function plot the graph of the input func 
    within the given interval [a,b).
    """
    # Your code goes here


def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    """
    Bisection method to find the root of a function within a given interval.

    Parameters:
    - func: The function for which the root is to be found.
    - a, b: Interval [a, b] within which the root is searched for.
    - tol: Tolerance level for checking convergence of the method.
    - max_iter: Maximum number of iterations.

    Returns:
    - root: Approximation of the root.
    
    Example
    --------
    >>> fun = lambda x: x**2 - x - 1
    >>> root = bisection_method(fun, 1, 2, max_iter=20)
    """

    # Check if the interval is valid (signs of f(a) and f(b) are different)
    # Your code goes here

    # Main loop starts here
    iter_count = 1
    while iter_count <= max_iter:
        # your code goes here
        
        iter_count += 1
    
    print("Warning! Exceeded the maximum number of iterations.")
    return root

# Example usage:
if __name__ == "__main__":
    # Define the function for which the root is to be found
    func = lambda x: x**2 - x - 1  # First Function
    
    # Uncomment the below line to use the Second Function
    # func = lambda x: x**3 - x**2 - 2*x + 1  # Second Function

    # Call plot_function to plot graph of the function
    # Your code goes here

    # Set the interval [a, b] for the search
    a_1 = 0; b_1 = 0;  # For first root (change the values as required)
    a_2 = 0; b_2 = 0;  # For second root (change the values as required)


    # Call the bisection method
    our_root_1 = # your code goes here
    our_root_2 = # your code goes here

    # Call SciPy method root, which we consider as a reference method.
    x0 = (a_1 + b_1)/2
    sp_result_1 = sp.optimize.root(func, x0)
    sp_root_1 = sp_result_1.x.item()

    x0 = (a_2 + b_2)/2
    sp_result_2 = sp.optimize.root(func, x0)
    sp_root_2 = sp_result_2.x.item()

    # Print the result
    print("1st root found by Bisection Method = {:0.8f}.".format(our_root_1))
    print("1st root found by SciPy = {:0.8f}".format(sp_root_1))

    print("2nd root found by Bisection Method = {:0.8f}.".format(our_root_2))
    print("2nd root found by SciPy = {:0.8f}".format(sp_root_2))
    
