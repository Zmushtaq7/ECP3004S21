# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Zaid Mushtaq
#
# Date: 2/24/21
# 
##################################################
#
# Sample Script for Assignment 5: 
# Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for the script my_A5_tests.py.
##################################################
##################################################
"""






##################################################
# Import Required Modules
##################################################

# import name_of_module

import numpy as np

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1
def variance(x):
    x_mean = np.average(x);
    n = len(x);
    sum = 0
    for xi in x:
        sum = sum + (xi-x_mean)**2
    return (1/n) * sum

# Exercise 2
def covariance(y, x):
    y_mean = np.average(y)
    x_mean = np.average(x)
    n = len(x)
    sum = 0
    for xi, yi in zip(x, y):
        sum = sum + (yi-y_mean)*(xi-x_mean)
    return (1/n) * sum

# Exercise 3
def ols_step(y, x):
    return covariance(y,x)/variance(x)
    
# Exercise 4
def ols_intercept(y, x, beta_1_hat):
    return np.average(y)-beta_1_hat*np.average(x)

# Exercise 5
def ssr(y, x, beta_0, beta_1):
    sum = 0
    for xi, yi in zip(x, y):
        sum = sum + (yi-beta_0-beta_1*xi)
    return sum

# Exercise 6
def min_ssr(y, x, beta_0_min, beta_0_max, beta_1_min, beta_1_max, step):
    min_SSR = 999999
    beta_0_list = range(beta_0_min, beta_0_max, step=(1/step))
    beta_1_list = range(beta_1_min, beta_1_max)
    i_min = -1
    j_min = -1
    for i, j in [range(len(beta_0_list)), range(len(beta_1_list))]:
        ssr = ssr(y, x, beta_0_list[i], beta_1_list[j])
        if(ssr < min_SSR):
            min_SSR = ssr
            i_min = i
            j_min = j
    return [beta_0_list[i_min], beta_1_list[j_min]]


# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstrings
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# The tests are implemented below -- but only
# when the script is run, not when it is imported. 


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    






##################################################
# End
##################################################
