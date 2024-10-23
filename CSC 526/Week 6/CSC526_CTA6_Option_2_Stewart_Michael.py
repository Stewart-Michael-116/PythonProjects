# CNN Classification of Cat and Dog

import tensorflow as tf
import seaborn as sns
import numpy as np
from PIL import Image
import glob
from collections import defaultdict
from tensorflow import keras
from tensorflow.keras import layers

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