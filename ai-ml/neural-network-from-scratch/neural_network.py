# Credits: Sentdex on Youtube at https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3
# Author: Nikhil Singla

import random

random.seed(1)  # Fixing seed to ensure replicability.

n = 5 # This is the number of neurons that input in our target neuron. Each i'th neuron has an input value, along with an associated weight.

# CURRENT NEURON
inputs = [round(random.random()*10, 2) for _ in range(n) ] # Random inputs, upto 2 decimal places between 0 and 10
weights = [round(random.random()*5, 2) for _ in range(n)] # Random weights, upto 2 decimal places between 0 and 5
bias = random.randint(0, 10)    # Random bias between 1 - 10 inclusive for the entire neuron as a whole

neuron_result = [i*w for i, w in zip(inputs, weights)]  # Multiply each of the inputs with their corresponding weights
output = sum(neuron_result) + bias  # Add each of the inputs, along with the bias to the final output of the neuron

print(output)