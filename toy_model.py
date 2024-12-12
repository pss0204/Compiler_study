import numpy as np

class ToyModel:
    def __init__(self):
        self.layers = [
            {'type': 'Linear', 'params': {'W': np.random.randn(1, 2), 'b': np.random.randn(1)}},
            {'type': 'Relu'}
        ]

    def relu(self, x):
        return np.maximum(x, 0)

    def forward(self, x):
        for layer in self.layers:
            if layer['type'] == 'Linear':
                x = np.dot(layer['params']['W'], x) + layer['params']['b']
            elif layer['type'] == 'Relu':
                x = self.relu(x)
        return x