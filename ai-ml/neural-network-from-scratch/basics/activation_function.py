# Reference: https://numpy.org/doc/stable/reference/routines.math.html
# Author: Nikhil Singla

import numpy as np
import matplotlib.pyplot as plt

class ActivationFunction:
    def test_function(self, given_inputs=None, activationFunction="ReLU"):
        """Takes in the inputs, along with specific activation function if necessary, and then returns 
        both the input and the output in the form of a tuple of values."""
        # Can take custom input, not necessary though.

        if given_inputs is None:
            self.inputs = np.arange(-100, 100, 1)
        else:
            self.inputs = np.array(given_inputs)

        self.output = None

        # Mapping activation function names to class methods for easier selection
        activation_methods = {
            "ReLU": self.ReLU_forward,
            "tanh": self.tanh_forward,
            "leakyReLU": self.leakyReLU_forward,
            "sigmoid": self.sigmoid_forward,
            "elu": self.elu_forward,
            "softmax": self.softmax_forward
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

    def leakyReLU_forward(self, inputs, alpha=0.1):
        self.output = np.where(inputs > 0, inputs, alpha * inputs)
        # Dot multiplication of the inputs with 0.1 for negative values, or just the straight positive value as we take the maximum.

    def sigmoid_forward(self, inputs):
        self.output =  1/(1 + np.exp(-inputs))
        # Inverse of 1 + e^-x is the sigmoid function

    def elu_forward(self, inputs, alpha=1.0):
        # Exponential Linear Unit, Smooth out negative values that approach to -alpha when x = -inf
        self.output = np.where(inputs >= 0, inputs, alpha*(np.exp(inputs) - 1))
        
    def softmax_forward(self, inputs):
        # Returns the probabilistic output as exponent of input / total value of inputs' exponent.
        # Probabilistic means that its behaviour is kind of messed up for the range of elements, as the higher elements have bigger weights.
        # Should be better demonstrated with custom range of inputs instead. 

        exp_term = np.exp(inputs)
        self.output = exp_term/np.sum(exp_term) 
        # Translates to e^x / sum of all e^x transformations of the input. 

    def get_output(self):
        # Gets the output 
        return self.output
    

if __name__ == "__main__":

    fig, ax = plt.subplots(2, 3)
    plt.axis([-110, 110, -0.1, 0.15]) # TODO: NEEDS FIXING TO ALL SUBPLOTS, NOT JUST THE LAST ONE.

    function_plotting = ActivationFunction()
    fig.suptitle("Graphs of Activation Functions")

    list_of_activation_functions = [ "ReLU", "tanh", "leakyReLU", "sigmoid", "elu", "softmax"]
    subplot_coordinates = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2]]
    colors_list = ["red", "blue", "green", "cyan", "magenta", "black"]

    for function_name, subplots_location, colors in zip(list_of_activation_functions, subplot_coordinates, colors_list):
        x_coor, y_coor = function_plotting.test_function(activationFunction=function_name)
        i, j = subplots_location
        ax[i, j].plot(x_coor, y_coor, color=colors)
        ax[i, j].set_title(function_name, color=colors)
        ax[i, j].set(xlabel='Inputs', ylabel='Outputs')

    # fig.set_size_inches(16,18)  # Good for image saving, not for plt.show()
    # plt.savefig("ai-ml/neural-network-from-scratch/basics/activation_functions.png") 

    # TODO:Draw lines to split quadrants
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())

    fig.tight_layout()
    plt.show()
