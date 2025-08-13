# Reference: https://numpy.org/doc/stable/reference/routines.math.html
# Author: Nikhil Singla
import numpy as np

class LossFunction:
    def calculate_loss(self, output, y):
        """Takes the output of the model, along with the intended target values of the model"""
        sample_losses = self.forward(output, y)
        average_data_loss = np.mean(sample_losses)
        
        return average_data_loss
    
class Categorical_Entropy_Loss(LossFunction):
    def forward(self, y_predicted, y_true):
        pass