# Credit: https://cs231n.github.io/neural-networks-case-study/
import numpy as np

def create_data(points=100, classes=3, dimensionality=2):
    X = np.zeros((points*classes, dimensionality))  # data matrix (each row = single example)
    y = np.zeros(points*classes, dtype='uint8')     # class labels

    for j in range(classes):
        ix = range(points*j,points*(j+1))
        r = np.linspace(0.0,1,points)                   # radius
        t = np.linspace(j*4,(j+1)*4,points) + np.random.randn(points)*0.2   # theta
        X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
        y[ix] = j

    return X, y

if __name__ == "__main__":
    # Lets visualize the data:
    import matplotlib.pyplot as plt


    N = 100 # number of points per class
    D = 2 # dimensionality
    K = 3 # number of classes

    X, y = create_data(N, K, D)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.Spectral)
    plt.show()