# Credits: Sentdex on Youtube at https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3
# Author: Nikhil Singla

import random
import numpy as np
from basics.activation_function import ActivationFunction
from basics.spiral_data import create_data

# Set seed for reproducibility
random.seed(1)
np.random.seed(1)

# ---------------- Dense Layer Class ----------------
class Layer_Dense:
    def __init__(self, number_of_inputs_to_each_neuron, number_of_neurons_in_the_layer):
        lowerbound = -1
        upperbound = 1

        # Initialize weights uniformly in [lowerbound, upperbound]
        self.weights = np.random.uniform(low=lowerbound, high=upperbound, size=(number_of_inputs_to_each_neuron, number_of_neurons_in_the_layer))
        self.biases = np.zeros((1, number_of_neurons_in_the_layer))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

# ---------------- Configuration ----------------
INPUT_NEURONS = 2           # Number of inputs per sample
HIDDEN_NEURONS = 10         # Neurons in the first (hidden) layer
OUTPUT_NEURONS = 3          # Single neuron in the output layer
BATCH_SIZE = 2              # Number of samples in a batch
ROUNDING_PRECISION = 2      # Decimal places for rounding input values

X, y = create_data()

# ---------------- Network Flow ----------------
# Initialize layers
layer_1 = Layer_Dense(INPUT_NEURONS, HIDDEN_NEURONS)
activation_layer = ActivationFunction()
layer_2 = Layer_Dense(HIDDEN_NEURONS, OUTPUT_NEURONS)

# Forward pass
layer_1.forward(X)
activation_layer.ReLU_forward(layer_1.output)

layer_2.forward(activation_layer.get_output())
activation_layer.softmax_forward(layer_2.output)

output = activation_layer.get_output()

# ---------------- Output ----------------
print("Final Output")
print(output)
