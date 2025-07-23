# Reference: https://numpy.org/doc/stable/reference/routines.math.html
# Author: Nikhil Singla

import numpy as np
import matplotlib.pyplot as plt

class ActivationFunction:
    def test_function(self, activationFunction="ReLU", given_inputs=None):
        # Can take custom input, not necessary though.

        if given_inputs is None:
            self.inputs = np.arange(-100, 100, 0.1)
        else:
            self.inputs = given_inputs

        self.output = None

        # Mapping activation function names to class methods for easier selection
        activation_methods = {
            "ReLU": self.ReLU_forward,
            "tanh": self.tanh_forward,
            "leakyReLU": self.leakyReLU_forward,
            "sigmoid": self.sigmoid_forward,
            "elu": self.elu_forward,
        }

        # Calling the selected activation function, only if it exists, or raising an error otherwise
        if activationFunction in activation_methods:
            activation_methods[activationFunction](self.inputs)
        else:
            raise ValueError(f"Unsupported activation function: {activationFunction}")

        # Getting the x coordinate or the inputs, and the y coordinate or the outputs
        return (self.inputs, self.output)

    def ReLU_forward(self, inputs):
        self.output = np.maximum(0, inputs)

    def tanh_forward(self, inputs):
        self.output = np.tanh(inputs)
        # Tanh function call for activation function

    def leakyReLU_forward(self, inputs):
        self.output = np.maximum(np.dot(inputs, 0.1), inputs)
        # Dot multiplication of the inputs with 0.1 for negative values, or just the straight positive value.

    def sigmoid_forward(self, inputs):
        self.output =  1/(1 + np.exp(-inputs))
        # Inverse of 1 + e^-x is the sigmoid function

    def elu_forward(self, inputs, alpha=1.0):
        # Exponential Linear Unit, Smooth out negative values that approach to -alpha when x = -inf
        self.output = np.where(inputs >= 0, inputs, alpha*(np.exp(inputs) - 1))
        
    def get_output(self):
        # Gets the output 
        return self.output

function_plotting = ActivationFunction()
x_coor, y_coor = function_plotting.test_function()

fig, ax = plt.subplots()
ax.plot(x_coor, y_coor)

# Draw lines to split quadrants
plt.show()