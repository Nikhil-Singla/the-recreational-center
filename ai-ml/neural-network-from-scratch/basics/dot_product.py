# Author: Nikhil Singla
# DOT PRODUCT

import random
import numpy as np

random.seed(1)

n = 5
input_range = 10
weights_range = 5

# CURRENT NEURON
inputs = [round(random.uniform(-1, 1) * input_range, 2) for _ in range(n)]
weights = [round(random.uniform(-1, 1) * weights_range, 2) for _ in range(n)]
bias = random.randint(0, 10)

# Modelling output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + inputs[3]*weights[3] + inputs[4]*weights[4] + bias
neuron_result = [i*w for i, w in zip(inputs, weights)]
output = sum(neuron_result) + bias
print(output)

output = np.dot(inputs, weights) + bias
print(output)

output = np.dot(weights, inputs) + bias     # The order of weights, inputs matters for higher order of matrices.
print(output)

# XXXXXXXX TESTING OUTPUT ON CONSOLE XXXXXXXX
# print(inputs, weights) # Checking inputs and weights.
# print(output)