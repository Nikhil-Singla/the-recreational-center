# Credits: Sentdex on Youtube at https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3
# Author: Nikhil Singla

import random
import numpy as np

random.seed(1)  # Fixing seed to ensure replicability.

# Configuration: number of inputs, and value ranges for inputs and weights
n = 5
input_range = 10
weights_range = 5
bias_range = 5      # Range of biases from -ve value to +ve value
neuron_count = 3    # Number of neurons in the neuron layer
decimal_places = 2  # Number of decimal places to round off the INPUTS/WEIGHTS/BIASES, nor the prodcuts etc.. 


# Neuron Layer: Generate random inputs, weights and bias in the specified ranges
inputs = [round(random.uniform(-1, 1) * input_range, decimal_places) for _ in range(n)]
weights = [[round(random.uniform(-1, 1) * weights_range, decimal_places) for _ in range(n)] for _ in range(neuron_count)] # Generating a number of neurons equal to neuron_count of size n
biases = [round(random.uniform(-1, 1) * bias_range, decimal_places) for _ in range(neuron_count)]


# Modelling output by using the formula for every set of neuron weights and biases with the given input.
output = [sum(i*w for i, w in zip(inputs, neuron_weights)) + neuron_bias        # Iterating over all the weights and biases one by one
          for neuron_weights, neuron_bias in zip(weights, biases)]          
print(type(output), output)

output = np.dot(weights, inputs) + biases   # Rounding occurs here automatically. Which is not seen in the raw code variant above.
print(type(output), output)

# XXXXXXXX SOME IMPORTANT THEORY XXXXXXXX
# Don't forget, multiplying a matrix of order a*b with a matrix of order b*c gives a resultant matrix of order a*c
# It is rows * columns, which means that the number of columns of the first matrix should match the rows of the second matrix in a dot product.

# XXXXXXXX TESTING OUTPUT ON CONSOLE XXXXXXXX
# print(inputs, weights) # Checking inputs and weights.
# print(output)

# XXXXXXXX ERRORS TO NOTE WHILE PROGRAMMING XXXXXXXX
# ERROR: weights = [round(random.uniform(-1, 1) * weights_range, 2) for _ in range(n)] * 3
# Doesn't create three unique weights, but actually the same weights are repeated thrice.