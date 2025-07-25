import random
import numpy as np

# Custom activation function class with a test interface
from basics.activation_function import ActivationFunction

# Getting spiral dataset of fixed number of points, classes and dimension. Default is 100 points, for each of the 3 classes in 2D space
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

# Generate synthetic input data with random floats between -1 and 1
# X = [[round(random.uniform(-1, 1), ROUNDING_PRECISION) for _ in range(INPUT_NEURONS)] for _ in range(BATCH_SIZE)]
# X = np.array(X)  # Convert to NumPy array for matrix operations

# Generate synthetic input data with random points forming a spiral on the graph.
X, y = create_data()

# ---------------- Network Flow ----------------
# Initialize layers
layer_1 = Layer_Dense(INPUT_NEURONS, HIDDEN_NEURONS)
activation_layer = ActivationFunction()
layer_2 = Layer_Dense(HIDDEN_NEURONS, OUTPUT_NEURONS)

# Forward pass
layer_1.forward(X)
activation_layer.ReLU_forward(layer_1.output)
layer_2.forward(layer_1.output)


# ---------------- Output ----------------

# Although it works for every layer, just looking at a single layer gives a better idea of the working.
print("Layer 1 Output")
print(layer_1.output[99])
print("Applying Activation ReLU")
print(activation_layer.get_output()[99])
