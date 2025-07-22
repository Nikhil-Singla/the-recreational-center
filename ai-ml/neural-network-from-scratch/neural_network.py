# Credits: Sentdex on Youtube at https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3
# Author: Nikhil Singla

import random

random.seed(1)  # Fixing seed to ensure replicability.

n = 5 # This is the number of neurons that input in our target neuron. Each i'th neuron has an input value, along with an associated weight.
input_range = 10  # Sets the max range of inputs, from -10 to 10, inclusive. 
weights_range = 5 # Sets the max range of wegihts, from -5 to 5, inclusive. 

# CURRENT NEURON
inputs = [round(random.uniform(-1, 1) * input_range, 2) for _ in range(n) ] # Random inputs, upto 2 decimal places between 0 and 10
weights = [round(random.uniform(-1, 1) * weights_range, 2) for _ in range(n)] # Random weights, upto 2 decimal places between 0 and 5
bias = random.randint(0, 10)    # Random bias between 0 - 10 inclusive for the entire neuron as a whole

# Modelling output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + inputs[3]*weights[3] + inputs[4]*weights[4] + bias
neuron_result = [i*w for i, w in zip(inputs, weights)]  # Multiply each of the inputs with their corresponding weights
output = sum(neuron_result) + bias  # Add each of the weighted inputs, along with the neuron bias to the final output of the neuron



# XXXXXXXX TESTING OUTPUT ON CONSOLE XXXXXXXX
# print(inputs, weights) # Checking inputs and weights.
# print(output)