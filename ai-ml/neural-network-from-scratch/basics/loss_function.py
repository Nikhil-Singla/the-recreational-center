# Reference: https://numpy.org/doc/stable/reference/routines.math.html
# Author: Nikhil Singla

import numpy as np

class LossFunction:
    def calculate_loss(self, output, y):
        """Takes the output of the model, along with the intended target values of the model"""
        sample_losses = self.forward(output, y)
        average_data_loss = np.mean(sample_losses)
        
        return average_data_loss, sample_losses
    
class CategoricalCrossEntropy_Loss(LossFunction):
    def forward(self, y_predicted, y_true):

        # Predicted values is an n x m array, where n is the samples, and m is the categories. 
        # pred[n][m] is the confidence predicted for the mth category in the nth sample
        # True values is either a one hot encoded or scalar array. 
        # Case 1 is an array of length n, and Case 2 is a n x m array.


        # Get total number of samples inputted.
        # We will use to implement categorical error
        number_of_elements = len(y_predicted)

        # y_predicted = np.clip(y_predicted, 1e-7, 1-1e-7) We can clip if we like
        # I prefer to add an epsilon factor to the prediction.
        # This doesn't solve overconfident predictions, but helps better detect 0 errors.
        y_predicted[y_predicted == 0] = 1e-16

        # Scalar values
        if len(y_true.shape) == 1:
            # If we have scalar predictions
            # For each element, we take the ith element where i E y_true.
            # This means that range goes through each of the n terms, and y_true is the correct category.             
            correct_predictions = y_predicted[range(number_of_elements), y_true]
        
        # One hot encoded values
        if len(y_true.shape) == 2:
            # Here, we instead multiply the two matrices and their relative terms.
            # After this, we add all the terms together. In either case, since we assume 
            # that the other categories are 0, we are only left with the correct predictions. 
            correct_predictions = np.sum(y_predicted*y_true, axis=1)


        # One hot encoded = [[0, 1], [1, 0]]. Implies we are given all the categories and their confidence.
        # Scalar Values = [0, 1]. Implies we are given the category that is correct.
        
        negative_log_likelihoods = -np.log(correct_predictions)
        return negative_log_likelihoods