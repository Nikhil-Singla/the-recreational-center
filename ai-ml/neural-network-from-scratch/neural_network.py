# Credits: Sentdex on Youtube at https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3
# Author: Nikhil Singla

import random
import numpy as np

from basics.activation_function import ActivationFunction
from basics.spiral_data import create_data
from basics.loss_function import CategoricalCrossEntropy_Loss

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
X, y = create_data(100, 3, 2)

# DEBUGGING CODE BELOW
# X = np.array([[0,0],
#                   [0,1],
#                   [1,0],
#                   [1,1]])
# y = np.array([0,0,0,1])   # AND labels

INPUT_NEURONS = X.shape[1]  # Number of input features per single sample. Assuming 0th shape is the number of total samples, as we are working in a batch

HIDDEN_NEURONS = 10         # Neurons in the first (hidden) layer. Gives the complexity of the AI model.

OUTPUT_NEURONS = max(y)+1   # Neuron size in the output layer, dependant on how many categories. 
                            # For its calculation, we are assuming each category shows up AT LEAST ONCE in the given y, starting from 0

# print(INPUT_NEURONS, OUTPUT_NEURONS) DBG

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

loss_function = CategoricalCrossEntropy_Loss()
loss, _ = loss_function.calculate_loss(output, y)

predicted_outputs = np.argmax(output, axis=1)
accuracy = np.mean(predicted_outputs == y)

# ---------------- Output ----------------

# print("Final Output")
# print(output, y) DBG
# print(output)    DBG

print("Loss")
# print(loss, negative) DBG
print(loss)

print("Accuracy")
print(accuracy)