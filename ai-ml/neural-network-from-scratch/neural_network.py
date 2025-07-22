import random
import numpy as np

random.seed(1)  # Fixing seed to ensure replicability.

# Configuration
input_neuron_count = 3  # Number of edges inputting to each neuron
neuron_count = 3        # Number of neurons in each layer
batch_size = 3          # Number of inputs in our batch
rounding = 2            # Number of decimal places to round

assert input_neuron_count == neuron_count, "We need to have equal number of neurons in the current layer as there are neuron inputs coming from the previous layer."

X = [[round(random.uniform(-1, 1), rounding) for _ in range(input_neuron_count)] for _ in range(batch_size)]  
# print(X): [[-0.73, 0.69, 0.53], [-0.49, -0.01, -0.1], [0.3, 0.58, -0.81]] with seed = 1

class Layer_Dense:
    def __init__(self):
        pass
    def forward(self):
        pass
