import numpy as np

import tensorflow as tf

import matplotlib.pyplot as plt

tf.compat.v1.disable_eager_execution()
sess = tf.compat.v1.InteractiveSession()

#In order to make the random numbers predictable, we will define fixed seeds for both Numpy and #TensorFlow.

np.random.seed(101)

tf.random.set_seed(101)

#Now, let’s generate some random data for training the Linear Regression Model.

# Generating random linear data

# There will be 50 data points ranging from 0 to 50

x = np.linspace(0, 50, 50)

y = np.linspace(0, 50, 50)

# Adding noise to the random linear data
x += np.random.uniform(-4, 4, 50)

y += np.random.uniform(-4, 4, 50)

x = x.reshape(-1,1)
y = y.reshape(-1,1)
n = len(x) # Number of data points

plt.figure(figsize=(10,8))
plt.title("Training Data")
plt.scatter(x,y, label="Training Data", color='red')
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()

with tf.name_scope("placeholders"):
    X = tf.compat.v1.placeholder(tf.float32, shape=[50,1])
    Y = tf.compat.v1.placeholder(tf.float32, shape=[50,1])
with tf.name_scope("weights"):
    W = tf.Variable(tf.compat.v1.random_normal((1,1)))
    b = tf.Variable(tf.compat.v1.random_normal((1,)))
with tf.name_scope("prediction"):
    y_pred = tf.matmul(X,W)+b
with tf.name_scope("loss"):
    l = tf.reduce_sum((Y - y_pred)**2)

with tf.name_scope("optim"):
    train_op = tf.compat.v1.train.AdamOptimizer(0.01).minimize(l)

with tf.name_scope("summaries"):
    loss_summary = tf.summary.scalar("loss",l)

train_writer = tf.compat.v1.summary.FileWriter('/tmp/lr-train',tf.compat.v1.get_default_graph())

n_steps = 1000
with tf.compat.v1.Session() as sess:
   sess.run(tf.compat.v1.global_variables_initializer())
   # Train model
   for i in range(n_steps):
      feed_dict = {X: x, Y: y}
      _, summary, loss = sess.run([train_op, loss_summary, l], feed_dict=feed_dict)
      weight, bias = sess.run([W, b])
      print("step %d, loss: %f Weight: %f bias: %f" % (i, loss, weight, bias))


    
# Plot fitted line
plt.figure(figsize=(10, 8))
plt.scatter(x, y, label="Training Data", color='red')
print(weight)
y_fit = x * weight[0][0] + bias[0]
plt.plot(x, y_fit, color='blue', label='Fitted Line')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Fitted Line vs Training Data")
plt.legend()
plt.grid(True)
plt.show()
