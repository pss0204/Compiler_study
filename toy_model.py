import numpy as np

class ToyModel:
    def __init__(self):
        self.W = np.random.randn(1, 2)
        self.b = np.random.randn(1)

    def relu(self, x):
        return np.maximum(x, 0)

    def forward(self, x):
        linear = np.dot(self.W, x) + self.b
        return self.relu(linear)