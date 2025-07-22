# Credits: Sentdex on Youtube at https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3
# Author: Nikhil Singla

import random

random.seed(1)  # Fixing seed to ensure replicability.

# Configuration: number of inputs, and value ranges for inputs and weights
n = 5
input_range = 10
weights_range = 5

# ONE NEURON: Generate random inputs, weights and bias in the specified ranges
inputs = [round(random.uniform(-1, 1) * input_range, 2) for _ in range(n) ]
weights = [round(random.uniform(-1, 1) * weights_range, 2) for _ in range(n)]
bias = random.randint(0, 10)

# Remaining 2 neurons in the 3 NEURON LAYER, that get the same inputs but have different sets of weights and biases to the neurons. 
weights2 = [round(random.uniform(-1, 1) * weights_range, 2) for _ in range(n)]
weights3 = [round(random.uniform(-1, 1) * weights_range, 2) for _ in range(n)]
bias2 = random.randint(0, 10)
bias3 = random.randint(0, 10)

# Modelling output

output = [sum([i*w for i, w in zip(inputs, weights)]) + bias,
          sum([i*w for i, w in zip(inputs, weights2)]) + bias2,
          sum([i*w for i, w in zip(inputs, weights3)]) + bias3
          ]

# XXXXXXXX TESTING OUTPUT ON CONSOLE XXXXXXXX
# print(inputs, weights) # Checking inputs and weights.
# print(output)