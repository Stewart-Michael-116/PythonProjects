# Michael Stewart Week 2 Critical Thinking
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

tf.compat.v1.disable_eager_execution()
sess = tf.compat.v1.InteractiveSession()

mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()

train_images = x_train.reshape(60000, 784)

test_images = x_test.reshape(10000, 784)

train_images = train_images.astype('float32')

test_images = test_images.astype('float32')


x_train, x_test = train_images / 255.0, test_images / 255.0


y_train = tf.keras.utils.to_categorical(y_train, 10)

y_test = tf.keras.utils.to_categorical(y_test, 10)

# Visualize Input Code Segment
def display_sample(num):

    #Print the one-hot array of this sample's label
    print(y_train[num]) 

    #Print the label converted back to a number
    label = y_train[num].argmax(axis=0)

    #Reshape the 768 values to a 28x28 image
    image = x_train[num].reshape([28,28])

    plt.title('Sample: %d  Label: %d' % (num, label))

    plt.imshow(image, cmap=plt.get_cmap('gray_r'))

    plt.show()

display_sample(1234)

#Visualize data being fed into the model

images = x_train[0].reshape([1,784])

for i in range(1, 500):

    images = np.concatenate((images, x_train[i].reshape([1,784])))

plt.imshow(images, cmap=plt.get_cmap('gray_r'))

plt.show()

# input images and target labels for the images.
input_images = tf.compat.v1.placeholder(tf.float32, shape=[None, 784])

target_labels = tf.compat.v1.placeholder(tf.float32, shape=[None, 10])

hidden_nodes = 4096
hidden2_nodes = 4096

input_weights = tf.Variable(tf.compat.v1.truncated_normal([784, hidden_nodes]))

input_biases = tf.Variable(tf.zeros([hidden_nodes]))

hidden_weights = tf.Variable(tf.compat.v1.truncated_normal([hidden_nodes, hidden2_nodes]))
hidden2_weights = tf.Variable(tf.compat.v1.truncated_normal([hidden2_nodes, 10]))  # From first hidden to second hidden

hidden_biases = tf.Variable(tf.zeros([hidden_nodes]))
hidden2_biases = tf.Variable(tf.zeros([10]))

input_layer = tf.matmul(input_images, input_weights)

hidden_layer = tf.nn.relu(input_layer + input_biases)
hidden2_layer = tf.nn.relu(hidden_layer + hidden_biases)

digit_weights = tf.matmul(hidden2_layer, hidden2_weights) + hidden2_biases

loss_function = tf.reduce_mean(tf.compat.v1.nn.softmax_cross_entropy_with_logits_v2(logits=digit_weights, labels=target_labels))

optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.8).minimize(loss_function)

correct_prediction = tf.equal(tf.argmax(digit_weights,1), tf.argmax(target_labels,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

tf.compat.v1.global_variables_initializer().run()

EPOCH = 20

BATCH_SIZE = 30

TRAIN_DATASIZE,_ = x_train.shape

PERIOD = TRAIN_DATASIZE//BATCH_SIZE

for e in range(EPOCH):

    idxs = np.random.permutation(TRAIN_DATASIZE)

    X_random = x_train[idxs]

    Y_random = y_train[idxs]

    for i in range(PERIOD):

        batch_X = X_random[i * BATCH_SIZE:(i+1) * BATCH_SIZE]

        batch_Y = Y_random[i * BATCH_SIZE:(i+1) * BATCH_SIZE]

        optimizer.run(feed_dict = {input_images: batch_X, target_labels:batch_Y})

    print("Training epoch " + str(e+1))

    print("Accuracy: " + str(accuracy.eval(feed_dict={input_images: x_test, target_labels: y_test})))

predictions = tf.argmax(digit_weights, axis=1)
predicted_labels = predictions.eval(feed_dict={input_images: test_images})
true_labels = np.argmax(y_test, axis=1)

misclassified_indices = np.where(predicted_labels != true_labels)[0]

wrong_answer_array = np.zeros(10)

for index in misclassified_indices:
    wrong_answer_array = y_train[index] + wrong_answer_array

print(wrong_answer_array)
