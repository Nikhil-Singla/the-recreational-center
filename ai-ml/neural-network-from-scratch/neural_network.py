import random
import numpy as np

random.seed(1)  # Fixing seed to ensure replicability.

# Configuration
input_neuron_count = 3  # Number of edges inputting to each neuron
neuron_count = 5        # Number of neurons in the first layer
final_output = 1        # Size of the final output layer
batch_size = 2          # Number of inputs in our batch
rounding = 2            # Number of decimal places to round the input

X = [[round(random.uniform(-1, 1), rounding) for _ in range(input_neuron_count)] for _ in range(batch_size)]  

class Layer_Dense:
    def __init__(self, number_of_inputs_to_each_neuron, number_of_neurons_in_the_layer):
        lowerbound = -1
        upperbound = 1

        self.weights = np.random.uniform(low=lowerbound, high=upperbound, size=(number_of_inputs_to_each_neuron, number_of_neurons_in_the_layer))
        self.biases = np.zeros((1, number_of_neurons_in_the_layer))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer_1 = Layer_Dense(input_neuron_count, neuron_count)
layer_2 = Layer_Dense(neuron_count, final_output)

layer_1.forward(X)
layer_2.forward(layer_1.output)
