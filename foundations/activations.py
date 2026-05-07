import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        z_sigmoid = []
        for i in range(0, len(z)):
            sigmoid = 1 / (1 + np.exp(-z[i]))
            z_sigmoid.append(np.round(sigmoid,5))
        return z_sigmoid

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        z_relu = []
        for i in range(0, len(z)):
            relu = np.maximum(0, z[i])
            z_relu.append(np.round(relu,5))
        return z_relu
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        
