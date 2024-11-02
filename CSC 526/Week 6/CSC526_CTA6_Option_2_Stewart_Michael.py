# CNN Classification of Cat and Dog

import tensorflow as tf
import seaborn as sns
import numpy as np
from PIL import Image
import glob
from collections import defaultdict
import keras
from keras import layers
import matplotlib.pyplot as plt

IMG_SIZE = (94, 125)

def pixels_from_path(file_path):

    im = Image.open(file_path)
    im = im.resize(IMG_SIZE)

    np_im = np.array(im)

    #matrix of pixel RGB values

    return np_im

 

shape_counts = defaultdict(int)

for i, cat in enumerate(glob.glob('cats/*')[:1000]):

    if i%100==0:

        print(i)

    img_shape = pixels_from_path(cat).shape

    shape_counts[str(img_shape)]= shape_counts[str(img_shape)]+ 1

 

shape_items = list(shape_counts.items())

shape_items.sort(key = lambda x: x[1])

shape_items.reverse()

 

# 10% of the data will automatically be used for validation

validation_size = 0.1

img_size = IMG_SIZE # resize images to be 374x500 (most common shape)

num_channels = 3 # RGB

sample_size = 8192 #We'll use 8192 pictures (2**13)

 

pixels_from_path(glob.glob('cats/*')[5]).shape

 

SAMPLE_SIZE = 2048

print("loading training cat images...")

cat_train_set = np.asarray([pixels_from_path(cat) for cat in glob.glob('cats/*')[:SAMPLE_SIZE]])

print("loading training dog images...")

dog_train_set = np.asarray([pixels_from_path(dog) for dog in glob.glob('dogs/*')[:SAMPLE_SIZE]])

 

valid_size = 512

print("loading validation cat images...")

cat_valid_set = np.asarray([pixels_from_path(cat) for cat in glob.glob('cats/*')[-valid_size:]])

print("loading validation dog images...")

dog_valid_set = np.asarray([pixels_from_path(dog) for dog in glob.glob('dogs/*')[-valid_size:]])

 

x_train = np.concatenate([cat_train_set, dog_train_set])

labels_train = np.asarray([1 for _ in range(SAMPLE_SIZE)]+[0 for _ in range(SAMPLE_SIZE)]) 
x_valid = np.concatenate([cat_valid_set, dog_valid_set])

labels_valid = np.asarray([1 for _ in range(valid_size)]+[0 for _ in range(valid_size)])

total_pixels = img_size[0] *img_size[1] * 3

fc_size = 512

 

inputs = keras.Input(shape=(img_size[1], img_size[0],3), name='ani_image')

x = layers.Flatten(name = 'flattened_img')(inputs) #turn image to vector.

 

x = layers.Dense(fc_size, activation='relu', name='first_layer')(x)

outputs = layers.Dense(1, activation='sigmoid', name='class')(x)

 

model = keras.Model(inputs=inputs, outputs=outputs)

from keras import optimizers

# Create a custom Adam optimizer with the updated learning rate argument
customAdam = optimizers.Adam(learning_rate=0.001)

# Compile the model
model.compile(optimizer=customAdam,  # Optimizer
              loss="mean_squared_error",  # Loss function to minimize
              metrics=["mean_squared_error"])  # List of metrics to monitor

print('# Fit model on training data')

# Train the model
history = model.fit(x_train, 
                    labels_train, 
                    batch_size=32, 
                    shuffle=True,  # Important since we loaded cats first, dogs second.
                    epochs=3,
                    validation_data=(x_valid, labels_valid))

# Summary of training
# Train on 4096 samples, validate on 2048 samples
# loss: ... - mean_squared_error: ... - val_loss: ...

import numpy as np
from keras import models, layers

# Define constants
fc_layer_size = 128
img_size = IMG_SIZE

# Build the convolutional model
conv_inputs = layers.Input(shape=(img_size[1], img_size[0], 3), name='ani_image')
conv_layer = layers.Conv2D(24, kernel_size=3, activation='relu')(conv_inputs)
conv_layer = layers.MaxPool2D(pool_size=(2, 2))(conv_layer)

conv_layer = layers.Conv2D(48, kernel_size=3, activation='relu')(conv_inputs)
conv_layer = layers.MaxPool2D(pool_size=(2, 2))(conv_layer)

conv_x = layers.Flatten(name='flattened_features')(conv_layer)  # Turn image to vector

conv_x = layers.Dense(fc_layer_size, activation='relu', name='first_layer')(conv_x)
conv_x = layers.Dense(fc_layer_size, activation='relu', name='second_layer')(conv_x)
conv_outputs = layers.Dense(1, activation='sigmoid', name='class')(conv_x)

conv_model = models.Model(inputs=conv_inputs, outputs=conv_outputs)

# Create a custom Adam optimizer
customAdam = optimizers.Adam(learning_rate=1e-4)

# Compile the model
conv_model.compile(optimizer=customAdam,  # Optimizer
                   loss="binary_crossentropy",  # Loss function to minimize
                   metrics=["binary_crossentropy", "mean_squared_error"])  # List of metrics to monitor

print('# Fit model on training data')

# Fit the model
history = conv_model.fit(x_train, 
                          labels_train.reshape(-1, 1),
                          batch_size=32, 
                          shuffle=True,
                          epochs=5,
                          validation_data=(x_valid, labels_valid.reshape(-1, 1))) 


# Make predictions
preds = conv_model.predict(x_valid)
preds = np.asarray([pred[0] for pred in preds])

# Calculate correlation coefficient
correlation = np.corrcoef(preds, labels_valid)[0][1]
print(correlation)  # Display the correlation
# Adding jitter to predictions
jitter_strength = 0.2
labels_jittered = labels_valid + np.random.normal(0, jitter_strength, labels_valid.shape)


sns.scatterplot(x= preds, y= labels_jittered)
# Optionally, you can add titles and labels
plt.title('Scatter Plot of Predictions vs. True Labels')
plt.xlabel('Predictions')
plt.ylabel('True Labels')

# Show the plot
plt.show()

cat_quantity = sum(labels_valid)

for i in range(1, 10):
    threshold = 0.1 * i
    print('threshold: ' + str(threshold))
    
    # Calculate the mean for predictions above the threshold
    valid_preds = preds[preds > threshold]
    if valid_preds.size > 0:
        mean_value = valid_preds.mean()
        print(mean_value)
    else:
        print('No predictions above the threshold')

print("First 10 predicted probabilities:", preds[:10])
print("First 10 true labels:", labels_valid[:10])

def animal_pic(index):

    img = Image.fromarray(x_valid[index])
    img.show()
    return

def cat_index(index):

    return conv_model.predict(np.asarray([x_valid[index]]))[0][0]

conv_model.save('conv_model_big.keras')

while(1):
    index = input("Type what index of photo you'd like to test:\n")

    if(index == 'exit'):
        break
    else:
        index = int(index)

    print("probability of being a cat: {}".format(cat_index(index)))
    animal_pic(index)