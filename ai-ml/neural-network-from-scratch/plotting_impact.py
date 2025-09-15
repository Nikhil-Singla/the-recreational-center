# Learning about the concept of optimization and the calculation


# This is how we get the impact of a basic function
# ie, by taking the slope of the tangent at that point.
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    # 2x^2
    return 2*x**2

p2_delta = 0.00001

x1 = 1
x2 = x1 + p2_delta

y1 = f(x1)
y2 = f(x2)

approximate_derivative = (y2 - y1) / (x2 - x1)
b = y1 - approximate_derivative*x1
print((x1, y1), (x2, y2), approximate_derivative)


# Now to improve the visualization:

# We first create a plot of all the continuous points of f(x) for x = [1, 50]
x = np.arange(0, 6, 0.01)
y = f(x)

plt.plot(x, y)

def approximate_TANGENT_line(x):
    return approximate_derivative*x + b

line_length = 1
line_range = [x1 - line_length, x1, x1 + line_length]

plt.plot([approximate_TANGENT_line(point) for point in line_range])

plt.show()