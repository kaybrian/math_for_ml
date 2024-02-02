# -*- coding: utf-8 -*-
"""

Original file is located at
    https://colab.research.google.com/drive/191MlU_Ngrq9yPN-iIM7GROQLbNc-eZn0
"""
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

"""Question
1.   Write a dynamic function to find the derivative of any function f(x)

"""



def find_derivative(f):
    """
      Calculate the derivative of a function f(x).
      Args:
        - f: The function for which the derivative
      Returns:
        - The derivative of f(x).
    """
    x = sp.symbols('x')
    f_deri = sp.diff(f, x)
    return f_deri

x = sp.symbols('x')
my_function = 4*x**7+ x**-1

# Calculate the derivative of my_function
derivative = find_derivative(my_function)
print("The derivative of the function is:", derivative)

"""
Question.
2.   Test the derivative function written with a quadratic equation of your choice

"""

#  i have the Funtion now of the Derivative *derivative*
x = sp.symbols('x')


# Define the function f(x) = 3x^2 + 2x - 5

f_x = 3*x**2 + 2*x - 5
# Calculate the derivative
derivative = find_derivative(f_x)
print("The derivative of the f(x) = 3x^2 + 2x - 5 is:", derivative)

# Define the function f(x) = 6x² + 11x - 35
f_x3 = 6*x**2 + 11 * x - 35
# Calculate the derivative
derivative = find_derivative(f_x3)
print("The derivative of the f(x) = 6x² + 11x - 35  is:", derivative)

# Define the function f(x) = 2x² - 4x - 2
f_x4 = 2*x**2 + 4 * x - 2
# Calculate the derivative
derivative = find_derivative(f_x4)
print("The derivative of the f(x) = 2x² - 4x - 2 is:", derivative)

#  Define the function f(x) = -4x² - 7x +12
f_x5 = -4*x**2 - 7 * x + 12
# Calculate the derivative
derivative = find_derivative(f_x5)
print("The derivative of the f(x) = -4x² - 7x +12 is:", derivative)

# Define the function f(x) = 20x² -15x - 10
f_x6 = 20 * x **2 - 15 * x - 10
# Calculate the derivative
derivative = find_derivative(f_x6)
print("The derivative of the f(x) = 20x² -15x - 10 is:", derivative)

"""Question
3.   Plot a graph of the quadratic Equation



"""

def quadratic_y_equation(quadratic_eq, x_value):
    """
      Calculate the y value given an x value in a quadratic equation using SymPy.

      Args:
      - quadratic_eq: The quadratic equation as a SymPy expression.
      - x_value: The x value for which to find the corresponding y value.

      Returns:
      - The y value corresponding to the given x value.
    """
    x = sp.symbols('x')
    y_expr = quadratic_eq.subs(x, x_value)
    return y_expr



def plot_graph(fun_x, x_values):
    """
      Plots a graph of of a Quadratic equation equation
      Calculates the y_values of a quadratic equation given the x_values

      Args:
        - fun_x': the quadratic Equation to be plotted
        - x_values: a list of x values to plot or get the y values

      Returns:
        - a plotted graph of the Quadratic equation
    """
    y_values = []

    # get a list of all the y values in the quadratic equation
    for i in x_values:
      y_value = quadratic_y_equation(fun_x, i)
      y_values.append(y_value)

    # plot the graphs, of the quadratic equation given the x and y values
    plt.style.use('dark_background')
    plt.plot(x_values, y_values)
    plt.xlabel('x values ')
    plt.ylabel('y values ')
    plt.title(f'Graph of y = {fun_x}')
    plt.grid(True)
    plt.show()





quadratic_eq = 4*x**2 + x**-1
# x value for which to find the corresponding y value
x_value = 1
x_values = np.linspace(-25, 25, 1000)
plot_graph(quadratic_eq, x_values)


# # Calculate the corresponding y value for x_value
# y_value = quadratic_y_equation(quadratic_eq, x_value)
# print("Corresponding y value for x =", x_value, ":", y_value)

"""Question 4
4. Create separate array of Minima and maxima

"""

def get_maxima_minima(func_x):
    # Calculate the derivative
    x = sp.symbols('x')
    derivative = sp.diff(func_x, x)

    # Find critical points by solving f'(x) = 0
    critical_points = sp.solve(derivative, x)

    # Calculate y values for critical points
    x_critical_points = []
    y_critical_points = []
    for point in critical_points:
        y_value = func_x.subs(x, point)
        x_critical_points.append(point)
        y_critical_points.append(y_value)

    return x_critical_points, y_critical_points

# Example usage:
quadratic_eq = 4*x**2 + x**-1

x_val, y_val = get_maxima_minima(quadratic_eq)
# get the max and min
for x, y in zip(x_val, y_val):
  print("x =", x, ", y =", y)

"""Question 5
5.   Finally, What is the global Minima and the Global maxima _
"""

def get_maxima_minima(func_x):
    """
      Calculate the maxima and minima points of a quadratic equation.

      Args:
      - func_x: The quadratic equation as a SymPy expression.

      Returns:
      - Lists of x and y values for the critical points (maxima and minima).
    """
    x = sp.symbols('x')
    derivative = sp.diff(func_x, x)
    critical_points = sp.solve(derivative, x)
    x_critical_points = []
    y_critical_points = []
    for point in critical_points:
        y_value = func_x.subs(x, point)
        x_critical_points.append(point)
        y_critical_points.append(y_value)
    return x_critical_points, y_critical_points

def plot_maxima_minima(quadratic_eq):
    """
      Plot the maxima and minima of a quadratic equation.

      Args:
      - quadratic_eq: The quadratic equation as a SymPy expression.

      Returns:
      - None (displays the plot).
    """
    x_values = np.linspace(-10, 100, 11234)
    y_values = sp.lambdify(x, quadratic_eq)(x_values)
    x_critical_points, y_critical_points = get_maxima_minima(quadratic_eq)
    plt.plot(x_values, y_values, label='Quadratic Equation')
    plt.plot(x_critical_points, y_critical_points, 'ro', label='Maxima/Minima')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Maxima and Minima of Quadratic Equation')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
x = sp.symbols('x')
quadratic_eq = x**2

plot_maxima_minima(quadratic_eq)
