# Credits: Sentdex on Youtube at https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3
# Author: Nikhil Singla

import random
import numpy as np

random.seed(1)  # Fixing seed to ensure replicability.

# Configuration
input_neuron_count = 3  # Number of edges inputting to each neuron
neuron_count = 5        # Number of neurons in the first layer
final_output = 1        # Size of the final output layer
batch_size = 2          # Number of inputs in our batch
rounding = 2            # Number of decimal places to round the input

# assert input_neuron_count == neuron_count, "We need to have equal number of neurons in the current layer as there are neuron inputs coming from the previous layer."
# Now we are trying to go beyond this for our calculations into matrices. Can be done with clever thinking.

X = [[round(random.uniform(-1, 1), rounding) for _ in range(input_neuron_count)] for _ in range(batch_size)]  
# print(X): [[-0.73, 0.69, 0.53], [-0.49, -0.01, -0.1], [0.3, 0.58, -0.81]] with seed = 1

class Layer_Dense:
    def __init__(self, number_of_inputs_to_each_neuron, number_of_neurons_in_the_layer):
        lowerbound = -1 # Lowerbound of weights
        upperbound = 1  # Upper bound of weights

        self.weights = np.random.uniform(low=lowerbound, high=upperbound, size=(number_of_inputs_to_each_neuron, number_of_neurons_in_the_layer))
        # Generate listing of weights automatically, of the shape given in the input. 
        # Number of rows = inputs, and number of neurons in a layer = columns, that is to say,
        # each column is a different neuron in the layer, and each row of a column corresponds
        # to one edge going into that neuron

        self.biases = np.zeros((1, number_of_neurons_in_the_layer))
        # Zeroing the biases in the beginning may not be always optimal. It might be better to redefine it to be

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer_1 = Layer_Dense(input_neuron_count, neuron_count)
# Getting fed from the number of input neurons, to each of the neruons in neuron_count

layer_2 = Layer_Dense(neuron_count, final_output)
# Since it takes the output from layer one, neuron_count is feeding into it, and the number of neurons outputted is matching what we need in the final output size

layer_1.forward(X)
# print(layer_1.output)

layer_2.forward(layer_1.output)
print(layer_2.output)