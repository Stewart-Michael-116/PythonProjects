import numpy as np
# Neuron

np.random.seed(0)

X = [[1, 2, 3, 4],
     [2, 4, 6, 8],
     [3, 6, 9, 12]]
print(X)

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer_Dense(4, 5)
layer2 = Layer_Dense(5, 2)

layer1.forward(X)
print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)


'''
weights = [[1, 1.5, 2, 4],
           [1, 1.5, 5, 5],
           [1, 0.4, 1, 5],
           ]

biases = [1,2,5]

weights2 = [[1, 1, 2],
           [2, 1.5, 3],
           [4, -2, 1],
           ]

biases2 = [-1,-2,4]

layer_1_output = np.dot(inputs, np.array(weights).T) + biases
layer_2_output = np.dot(layer_1_output, np.array(weights2).T) + biases
print(layer_2_output)
'''