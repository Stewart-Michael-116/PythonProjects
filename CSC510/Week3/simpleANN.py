# https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=1
# I used a tutorial online to help me grasp of neural networks, based on this youtube series, I implemented the assignment here.

# My AI generates an amount of data specified by the user. This data is in 3 spirals on an XY graph. The AI then guesses which points belong to which spiral. 
# The optimization is randomizing the best weights we have found and seeing if it produces a better loss value.

# These are all the imports needed for each calculation.
import numpy as np
import nnfs
import matplotlib.pyplot as plt
from nnfs.datasets import spiral_data

#This initializes our random seed and nnfs
nnfs.init()
np.random.seed(0)

#Here is an implementation of the ReLU or rectified linear activation function. we use this on the first layer of the neural network
class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

# this is the implementation of a layer. This involves different neurons, inputs, and weights.
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

#This is my implementation of a softmax activation function
class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis = 1, keepdims = True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities

# This will calculate my loss depending on the loss function you give it.
class Loss:
    def calculate(self, output, y):
        sample_losses = self.forward(output,y)
        data_loss = np.mean(sample_losses)
        return data_loss
    
# This is the -log or categorical cross entropy loss function. This uses a -log activation function so that we can make sure our values don't grow too large and we keep the data
# from values that get cut off by the rectified linear activation function.
class Loss_CategoricalCrossentropy(Loss):
    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)

        if len(y_true.shape) == 1:
            correct_confidences = y_pred_clipped[range(samples),y_true]
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred_clipped*y_true, axis=1)

        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods

# First prompt        
data_amount = input("\nWelcome to Michael's first AI! This script will \nautomatically generate a dataset of 3 different spirals, and the AI will need to guess which \ndata points belong to each spiral. Please enter a number of data points per spiral. Around 100 is normal:\n")
X, y = spiral_data(int(data_amount), 3)
plt.scatter(X[:, 0],X[:,1], c=y, s =40, cmap = 'brg')
plt.show()

# Create neural network
layer1 = Layer_Dense(2, 3)
activation1 = Activation_ReLU()
layer2 = Layer_Dense(3, 3)
activation2 = Activation_Softmax()

# Put data through network
layer1.forward(X)
activation1.forward(layer1.output)
layer2.forward(activation1.output)
activation2.forward(layer2.output)
#print(activation2.output[:5])

loss_function = Loss_CategoricalCrossentropy()
loss = loss_function.calculate(activation2.output,y)
#print("Loss:", loss)

lowest_loss = 9999999
best_layer1_weights = layer1.weights.copy()
best_layer2_weights = layer2.weights.copy()
best_layer1_biases = layer1.biases.copy()
best_layer2_biases = layer2.biases.copy()
iteration_list = []

for iteration in range(9999999999999999999999):
    layer1.weights += 0.05 * np.random.randn(2,3)
    layer1.biases += 0.05 * np.random.randn(1,3)
    layer2.weights += 0.05 * np.random.randn(3,3)
    layer2.biases += 0.05 * np.random.randn(1,3)

    layer1.forward(X)
    activation1.forward(layer1.output)
    layer2.forward(activation1.output)
    activation2.forward(layer2.output)

    loss = loss_function.calculate(activation2.output, y)

    predictions = np.argmax(activation2.output, axis=1)
    accuracy = np.mean (predictions == y)

    if loss < lowest_loss:
        print("New set of weights found that are better, iteration number:", iteration, "loss:", loss, "accuracy:", accuracy)
        best_layer1_weights = layer1.weights.copy()
        best_layer2_weights = layer2.weights.copy()
        best_layer1_biases = layer1.biases.copy()
        best_layer2_biases = layer2.biases.copy()
        lowest_loss = loss
    else:
        layer1.weights = best_layer1_weights.copy()
        layer1.biases = best_layer1_biases.copy()
        layer2.weights = best_layer2_weights.copy()
        layer2.biases = best_layer2_biases.copy()

'''
This was a failed attempt to plot what the correct guesses were by the neural network. If I had more time I would figure out how to add each point to a new array based on if
it is correct or not

    iterationGraph = -1
    correct = []
    correctColor = []
    for node in X:
        iterationGraph += 1
        if(predictions[iterationGraph]==y[iterationGraph]):
            correct.append(node)
            correctColor.append(y[iterationGraph])

    plt.scatter(correct[:, 0],correct[:,1], c=correctColor, s =40, cmap = 'brg')
    plt.show()


Here is old code from me doing tutorials and figuring out neural networks.

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