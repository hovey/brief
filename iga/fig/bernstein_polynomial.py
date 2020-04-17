import math
import sys
import numpy as np

def bernstein_polynomial(i, p, nti):
    """ 
    Computes the Bernstein polynomial coefficient for 
    control point i with 
    polynomial degreee p
    for an 1D array t, t = [0, 1] broken into 
    nti number of time intervals in [0, 1], equidistant

    i is non-negative integer 0, 1, 2, ... p
    p is interger >= 1
    nti is integer >= 2
    """
    t = np.linspace(0, 1, nti+1)
    bp = math.factorial(p) / (math.factorial(i) * math.factorial(p-i)) * t**i * (1-t)**(p-i)
    return bp
