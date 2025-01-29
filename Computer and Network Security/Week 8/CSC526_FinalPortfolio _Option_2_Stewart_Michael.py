# Week 8 portfolio project
# the source code from the assignment did not have the imports listed, so I had to change
# some function calls in order for them to be called correctly

# This is where the imports are
import pandas as pd
import numpy as np
from sklearn import datasets
import tensorflow as tf
import keras
import random

# Here is where I define the models
def define_models(n_input, n_output, n_units):
    # Encoder inputs, encoderLSTM layer, and outputs
    encoder_inputs = keras.layers.Input(shape=(None, n_input))
    encoder = keras.layers.LSTM(n_units, return_state=True)
    encoder_outputs, state_h, state_c = encoder(encoder_inputs)
    encoder_states = [state_h, state_c]
    # Pass on hidden and case state

    # Decoder inputs, LTSM layers, dense, and outputs
    decoder_inputs = keras.layers.Input(shape=(None, n_output))
    decoder_lstm = keras.layers.LSTM(n_units, return_sequences=True, return_state=True)
    decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state=encoder_states)
    decoder_dense = keras.layers.Dense(n_output, activation='softmax')
    decoder_outputs = decoder_dense(decoder_outputs)

    model = keras.Model([encoder_inputs, decoder_inputs], decoder_outputs)

    encoder_model = keras.Model(encoder_inputs, encoder_states)

    decoder_state_input_h = keras.layers.Input(shape=(n_units,))
    decoder_state_input_c = keras.layers.Input(shape=(n_units,))
    decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]

    decoder_outputs, state_h, state_c = decoder_lstm(decoder_inputs, initial_state=decoder_states_inputs)
    decoder_states = [state_h, state_c]
    decoder_outputs = decoder_dense(decoder_outputs)

    decoder_model = keras.Model([decoder_inputs] + decoder_states_inputs, [decoder_outputs] + decoder_states)

    return model, encoder_model, decoder_model

def predict_sequence(infenc, infdec, source, n_steps, cardinality):

    state = infenc.predict(source)

    target_seq = np.array([0.0 for _ in range(cardinality)]).reshape(1, 1, cardinality)

    output = list()

    for t in range(n_steps):

        yhat, h, c = infdec.predict([target_seq] + state)

        output.append(yhat[0, 0, :])

        state = [h, c]

        target_seq = yhat

    return np.array(output)

def generate_sequence(length, n_unique):
    return [random.randint(1, n_unique-1) for _ in range(length)]

def get_dataset(n_in, n_out, cardinality, n_samples):
    # Creates dataset which makes a target that has the first arguments reversed.
    X1, X2, y = list(), list(), list()

    for _ in range(n_samples):

        source = generate_sequence(n_in, cardinality)

        target = source[:n_out]
        target.reverse()

        target_in = [0] + target[:-1]

        src_encoded = keras.utils.to_categorical(source, num_classes=cardinality)
        tar_encoded = keras.utils.to_categorical(target, num_classes=cardinality)
        tar2_encoded = keras.utils.to_categorical(target_in, num_classes=cardinality)

        X1.append(src_encoded)
        X2.append(tar2_encoded)
        y.append(tar_encoded)

    X1 = np.array(X1).reshape(-1, n_in, cardinality)  
    X2 = np.array(X2).reshape(-1, n_out, cardinality)  
    y = np.array(y).reshape(-1, n_out, cardinality)  

    return X1, X2, y

# Returns the index of the max value in the array, which returns the class in our code.
def one_hot_decode(encoded_seq):

    return [np.argmax(vector) for vector in encoded_seq]

# Define features of the dataset
n_features = 50 + 1

n_steps_in = 6

n_steps_out = 3

X1, X2, y = get_dataset(n_steps_in, n_steps_out, n_features, 1)

print(X1.shape, X2.shape, y.shape)

print('X1=%s, X2=%s, y=%s' % (one_hot_decode(X1[0]), one_hot_decode(X2[0]), one_hot_decode(y[0])))

# Compile and train our model.
train, infenc, infdec = define_models(n_features, n_features, 128)

train.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

n_samples = 1000
n_epochs = 2000    
batch_size = 64  
X1_train, X2_train, y_train = get_dataset(n_steps_in, n_steps_out, n_features, n_samples)

train.fit([X1_train, X2_train], y_train, epochs=n_epochs, batch_size=batch_size, verbose=1)



total, correct = 100, 0
# veryify accuracy by going through predictions and measuring accuracy.
for _ in range(total):
    X1, X2, y = get_dataset(n_steps_in, n_steps_out, n_features, 1)
    source = np.expand_dims(X1[0], axis=0)  
    state = infenc.predict(source) 

    target_seq = np.zeros((1, 1, n_features)) 
 
    output = list()

    for t in range(n_steps_out):
        yhat, h, c = infdec.predict([target_seq] + state) 

        output.append(yhat[0, 0, :])

        state = [h, c]

        target_seq = yhat.reshape(1, 1, n_features)

    print("X={}, y={}, yhat={}".format(one_hot_decode(X1[0]),one_hot_decode(y[0]),one_hot_decode(np.array(output))))
    if np.array_equal(one_hot_decode(y[0]), one_hot_decode(np.array(output))):
        correct += 1

print('Accuracy: %.2f%%' % (float(correct) / float(total) * 100.0))


