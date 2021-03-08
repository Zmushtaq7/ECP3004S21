# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Zaid Mushtaq 
#
# Date: 3/8/21
# 
##################################################
#
# Sample Script for Midterm Exam: 
# Module with Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for a script that you might call
# my_midterm_tests.py (but is not graded).
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


def in_budget(x:int, y:int, p_x:float, p_y:float, w:float) -> bool:
    """
    Preconditions: x, y, w >= 0 and p_x, p_y > 0
    
    Calculates returns a boolean indicator 
    of whether the consumer's expenditure 
    is less than or equal to wealth.
    
    >>> in_budget(3, 1, 10, 25, 100)
    True
    >>> in_budget(2, 2, 15, 20, 100)
    True
    >>> in_budget(5, 3, 10, 25, 100)
    False
    
    """
    total_cost = (x*p_x)+(y*p_y)
    if w >= total_cost:
        return True
    return False



# Exercise 2


def calc_bundle(p_x, p_y, w, alpha) -> type:
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= alpha <= 1
    
    Calculates calculates the consumer's optimal bundle of goods
    for a consumer with Cobb-Douglass utility function.
    
    >>> calc_bundle(10, 20, 120, 1.0/3.0)
    [4.0, 4.0]
    >>> calc_bundle(10, 25, 100, .5)
    [5.0, 2.0]
    >>> calc_bundle(10, 25, 100, 2.0/3.0)
    [6.667, 1.333]
    
    """
    x_star = (alpha/p_x)*w
    y_star = ((1-alpha)/p_y)*w
    
    return [x_star, y_star]



# Exercise 3


def y_solve(x_star, p_x, p_y, w) -> type:
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= x_star <= w/p_x
    
    Calculates the remaining expenditure on good y, 
    given an expenditure x_star in good x.
    
    >>> y_solve(5, 5, 10, 100)
    7.5
    >>> y_solve(5, 10, 25, 100)
    2.0
    >>> y_solve(7, 10, 25, 100)
    1.2
    
    """
    
    return (w-x_star*p_x)/p_y


# Exercise 4


def one_loop_bundle(p_x, p_y, w, alpha, step) -> type:
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= alpha <= 1
    
    Calculates the consumer's optimal bundle of goods
    for a consumer with Cobb-Douglass utility function.
    It searches over a loop on x_star and assigns the remaining
    wealth to y using y_solve.
    
    >>> one_loop_bundle(5, 10, 100, 0.25, 0.01)
    [5.0, 7.5]
    >>> one_loop_bundle(10, 25, 100, .5, .1)
    [5.0, 2.0]
    >>> one_loop_bundle(25, 25, 100, .5, .1)
    [2.0, 2.0]
    
    """
    max_util = -99999
    x_list = np.arange(0, int(w/p_x), step)
    y_star = 0
    x_star = 0
    for x in x_list:
        y_candidate = y_solve(x, p_x, p_y, w)
        if max_util < x**alpha*y_candidate**(1-alpha):
            max_util = x**alpha*y_candidate**(1-alpha)
            x_star = x
            y_star = y_candidate
        
    return [x_star, y_star]



# Exercise 5


def util_in_budget(x, y, p_x, p_y, w, alpha) -> type:
    """Calculates the value of the Cobb-Douglass utility
    function for consumption goods x and y with exponent alpha.
    It restricts x and y to non-negative values and 
    alpha to the unit interval.
    It also restricts the calculation to bundles [x, y] within budget w, 
    otherwise it assigns zero.
    
    >>> util_in_budget(4, 4, 10, 20, 120, 1.0/3.0)
    4.0
    >>> util_in_budget(2, 2, 25, 25, 100, .5)
    2.0
    >>> util_in_budget(-1, 4, 100, 100, 100, .5)
    0.0
    >>> util_in_budget(4, -1, 100, 100, 100, .5)
    0.0
    >>> util_in_budget(4, 4, 100, 100, 100, 1.1)
    0.0    
    """
    
    if x <= 0 or y <= 0 or alpha > 1.0 or alpha < 0.0:
        return 0.0
    elif in_budget(x, y, p_x, p_y, w):
        return x**alpha*y**(1-alpha)
    return 0.0





# Exercise 6


def two_loop_bundle(p_x, p_y, w, alpha, step) -> type:
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= alpha <= 1
    
    Calculates the consumer's optimal bundle of goods
    for a consumer with Cobb-Douglass utility function.
    It searches over two loops on x_star and y_star.
    
    Note that there is no error handling
    because that is taken care of in util_in_budget() and np.arange(). 
    
    >>> two_loop_bundle(10, 25, 100, 0.5, 0.01)
    [5.0, 2.0]
    >>> two_loop_bundle(25, 25, 100, .5, .01)
    [2.0, 2.0]
    >>> two_loop_bundle(10, 20, 120, 1.0/3.0, .01)
    [4.0, 4.0] 
    """
    
    x_star_list = np.arange(0, w/p_x, step)
    y_star_list = np.arange(0, w/p_y, step)
    i_max = 0
    j_max = 0
    max_util = 0
    for i in range(len(x_star_list)):
        for j in range(len(y_star_list)):
            cur_util = util_in_budget(x_star_list[i], y_star_list[j], p_x, p_y, w, alpha)
            if cur_util > max_util:
                max_util = cur_util
                i_max = i
                j_max = j
    
    return [x_star_list[i_max], y_star_list[j_max]]



# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstrings above
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# Add code so that the tests are implemented below 
# -- but only when the script is run,
# not when it is imported. 


if __name__ == "__main__":
    import doctest
    doctest.testmod()








##################################################
# End
##################################################

