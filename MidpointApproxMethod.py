import numpy as np
import matplotlib.pyplot as plt

def plot_function(func, a, b):
    """
    This function plot the graph of the input func 
    within the given interval [a,b).
    """
    # Your code goes here

def midpoint_approx(func, a, b, N):
    '''Compute the Midpoint Approximation of Definite Integral of a function over the interval [a,b].

    Parameters
    ----------
    func : function
           Vectorized function of one variable
    a , b : numbers
        Endpoints of the interval [a,b]
    N : integer
        Number of subintervals of equal length in the partition of [a,b]

    Returns
    -------
    float
        Approximation of the definite integral by Midpoint Approximation.
    '''

    # Your code goes here
    return result

if __name__ == "__main__":
    # 1st Function to be integrated
    func_1 = lambda x : x/(x**2 + 1)
    # Indefinite Integral of the function
    antiderivative_1 = # Your code goes here
    
    # 2nd Function to be integrated
    func_2 = lambda x : np.exp(x)
    # Indefinite Integral of the function
    antiderivative_2 = # Your code goes here
    
    # End points for 1st Function
    a1 = 0; b1 = 0;  # Change the values as required
    # End points for 2nd Function
    a2 = 0; b2 = 0;  # Change the values as required

    # Call the function to Plot the graph of the functions
    # Your code goes here
    
    # Number of partition for 1st Function
    N1 = 0 # Change the value as required
    # Number of partition for 2nd Function
    N2 = 0 # Change the value as required

    # Call midpont_method to compute Midpoint Approximation:
    midpoint_approx_1 = # Your code for 1st function
    midpoint_approx_2 = # Your code for 2nd function
    
    # Calculate the true value of the definite integral
    definite_integral_1 = antiderivative_1(b) - antiderivative_1(a)  # For 1st Function
    definite_integral_2 = antiderivative_2(b) - antiderivative_2(a)  # For 2nd Function

    # Calculate the absolute error between the approximate value and true value
    error_1 = np.abs(midpoint_approx_1 - definite_integral_1)  # For 1st Function
    error_2 = np.abs(midpoint_approx_2 - definite_integral_2)  # For 2nd Function

    print("Subinterval width = {:0.6f}".format((b-a)/N))
    print("Midpoint Approximation for 1st Function = {:0.6f}".format(midpoint_approx_1))
    print("Actual Value for 1st Function = {:0.6f}".format(definite_integral_1))
    print("Absolute error between the above methods ={:0.8f}".format(error_1))

    print("Midpoint Approximation for 2nd Function = {:0.6f}".format(midpoint_approx_2))
    print("Actual Value for 2nd Function = {:0.6f}".format(definite_integral_2))
    print("Absolute error between the above methods ={:0.8f}".format(error_2))


    