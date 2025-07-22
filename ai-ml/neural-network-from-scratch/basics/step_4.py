# Credits: Sentdex on Youtube at https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3
# Author: Nikhil Singla

import random
import numpy as np

random.seed(1)  # Fixing seed to ensure replicability.

# Configuration
input_neuron_count = 3  # Number of edges inputting to each neuron
input_range = 10
weights_range = 5
bias_range = 5
neuron_count = 3        # Number of neurons in each layer
decimal_places = 2
batch_size = 3          # Number of inputs in our batch

assert input_neuron_count == neuron_count, "We need to have equal number of neurons in the current layer as there are neuron inputs coming from the previous layer."

# Neuron Layer

# We are now generating inputs to a total count of "batch_size"
inputs = [[round(random.uniform(-1, 1) * input_range, decimal_places) for _ in range(input_neuron_count)] for _ in range(batch_size)]  
weights = [[round(random.uniform(-1, 1) * weights_range, decimal_places) for _ in range(input_neuron_count)] for _ in range(neuron_count)]
biases = [round(random.uniform(-1, 1) * bias_range, decimal_places) for _ in range(neuron_count)]

# Output: Rounding occurs automatically in np.dot
# Our input is of dimension input_neuron_count * batch_size and our weights is of dimension input_neuron_count * neuron_count.
# To take the correct dot product, we need to Transpose one of our matrix. Logically thinking, it'd be the wegiht matrix as we want to multiply
# each row of the input matrix (which is one of the elements in our batch) to the entire column of matrix weight. 
layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
# In this manner, each element of the input batch, is multiplied to each neuron layer of weights, biases, and in our output matrix,
# each row is the array of outputs for one input element passing through our neurons. Giving us a total of "batch_size" output elements.

print("First Layer Outputs: \n", layer1_outputs)
# Prints out the output matrix layer of shape batch_size * neuron_count. To note is that the biases are added automatically to each row, thus getting us the proper result.

# SECOND Neuron Layer: Technically, we are overwriting the important stuff in the layers, but for a one time pass, its okay. 
weights = [[round(random.uniform(-1, 1) * weights_range, decimal_places) for _ in range(input_neuron_count)] for _ in range(neuron_count)]
biases = [round(random.uniform(-1, 1) * bias_range, decimal_places) for _ in range(neuron_count)]

layer2_outputs = np.dot(layer1_outputs, np.array(weights).T) + biases   # The output from layer one is now fed into the second neuron layer, which lets us get another set of outputs.
print("Second Layer Outputs: \n", layer2_outputs)

# We notice that since we did not confine the values between positive and negative one, within just 2 layers, we have somewhat of an explosion of values from our initial input set. 
# Input range lied between -ve and +ve 10, but our layer2_outputs have reached beyond the range of -ve nad +ve 200.