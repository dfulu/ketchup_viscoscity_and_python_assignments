USER = 'James Fulton'
USER_ID = 'njzc77'

from __future__ import division
import numpy as np #import necessary functions
import matplotlib.pyplot as pyplot

def f(x):
	''' returns the function xsin(x) '''
	return x*np.sin(x)

def f_prime_analytic(x):
	''' returns the derivative of function f, solved analytically'''
	return np.sin(x) + x*np.cos(x)

def f_prime_numeric(x):
	''' returns the derivative of the function f, approximated numerically using backwards difference method'''
	return (f(x)-f(x-0.25))/0.25

x_values = np.linspace(-np.pi, np.pi, 100) #set array of x values to test
ya_values = f_prime_analytic(x_values)
yn_values = f_prime_numeric(x_values)
pyplot.figure(figsize=(8,3))
pyplot.plot(x_values, ya_values, color='green', label='Analytic Drivative')
pyplot.plot(x_values, yn_values, color='blue', label='Numeric Drivative')
pyplot.xlabel('x - no units')
pyplot.ylabel("f'(x) - no units")
pyplot.legend()
pyplot.title("Comparison Between Numerical and Analytical Derivatives of f(x)")
pyplot.show()

ANSWER1='the estimate gets closer and closer to the true value up until when dx becomes of the order e-14. Smaller than this and it gets worse. This is because the inexactness of the numbers stored become significant at this small a number'