import numpy as np
import nnfs
nnfs.init()

layer_outputs = [[3,3,3],
                 [3,3,3],
                 [3,3,3]]

exp_values = np.exp(layer_outputs)

print(np.sum(layer_outputs, axis = 1, keepdims = True))

norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True)