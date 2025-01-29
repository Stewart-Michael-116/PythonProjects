# Michael Stewart Critical Thinking 4 Option 2
# Logistic Regression Modeling
# Generate synthetic data
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# need this for v1 tensorflow
tf.compat.v1.disable_eager_execution()
sess = tf.compat.v1.InteractiveSession()

N = 100

######## Not needed, used for previous assignent ########
# np.random.seed(101)

# tf.random.set_seed(101)

# Zeros form a Gaussian centered at (-1, -1)
#########################################################

x_zeros = np.random.multivariate_normal(

    mean=np.array((-1, -1)), cov=.1*np.eye(2), size=(N//2,))

y_zeros = np.zeros((N//2,))


x_ones = np.random.multivariate_normal(

    mean=np.array((1, 1)), cov=.1*np.eye(2), size=(N//2,))

y_ones = np.ones((N//2,))

x_np = np.vstack([x_zeros, x_ones])

y_np = np.concatenate([y_zeros, y_ones])

x_ones_x = [point[0] for point in x_ones]
x_ones_y = [point[1] for point in x_ones]

x_zeros_x = [point[0] for point in x_zeros]
x_zeros_y = [point[1] for point in x_zeros]

plt.figure(figsize=(10,8))
plt.title("Training Data")
plt.scatter(x_zeros_x,x_zeros_y, label="Zeros", color='red')
plt.scatter(x_ones_x,x_ones_y, label="Ones", color='blue')
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()

plt.show()

with tf.name_scope("placeholders"):

  x = tf.compat.v1.placeholder(tf.float32, (N, 2))

  y = tf.compat.v1.placeholder(tf.float32, (N,))

with tf.name_scope("weights"):

  W = tf.Variable(tf.random.normal((2, 1)))

  b = tf.Variable(tf.random.normal((1,)))

with tf.name_scope("prediction"):

  y_logit = tf.squeeze(tf.matmul(x, W) + b)

  y_one_prob = tf.sigmoid(y_logit)

  y_pred = tf.round(y_one_prob)

  with tf.name_scope("loss"):

    entropy = tf.nn.sigmoid_cross_entropy_with_logits(logits=y_logit, labels=y)


    l = tf.reduce_sum(entropy)

with tf.name_scope("optim"):

     train_op = tf.compat.v1.train.AdamOptimizer(.01).minimize(l)

with tf.name_scope("summaries"):

    tf.summary.scalar("loss", l)

    merged = tf.compat.v1.summary.merge_all()

train_writer = tf.compat.v1.summary.FileWriter('logistic-train', tf.compat.v1.get_default_graph())

init = tf.compat.v1.global_variables_initializer()
sess.run(init)


# Run epochs to train model.
num_epochs = 1000
for epoch in range(num_epochs):
    train_op_result, loss_value = sess.run([train_op, l], feed_dict={x: x_np, y: y_np})

    print(f"Epoch {epoch}, Loss: {loss_value}")

    if epoch % 25 == 0 and epoch <= 150:
        y_pred_np = sess.run(y_pred, feed_dict={x: x_np})
        
        plt.figure(figsize=(10, 8))
        plt.title("Training Data with Predictions after Epoch %d" % epoch)
        plt.scatter(x_zeros_x, x_zeros_y, label="Zeros", color='red')
        plt.scatter(x_ones_x, x_ones_y, label="Ones", color='blue')

        predicted_ones_x = x_np[y_pred_np.flatten() == 1][:, 0]
        predicted_ones_y = x_np[y_pred_np.flatten() == 1][:, 1]
        predicted_zeros_x = x_np[y_pred_np.flatten() == 0][:, 0]
        predicted_zeros_y = x_np[y_pred_np.flatten() == 0][:, 1]

        plt.scatter(predicted_ones_x, predicted_ones_y, label="Model Predicted One", marker='x', color='purple', s=125)
        plt.scatter(predicted_zeros_x, predicted_zeros_y, label="Model Predicted Zero", marker='x', color='yellow', s=125)

        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.legend()
        plt.show()

y_pred_np = sess.run(y_pred, feed_dict={x: x_np})

plt.figure(figsize=(10, 8))
plt.title("Final Training Data with Predictions After 1000 Epochs")
plt.scatter(x_zeros_x, x_zeros_y, label="Zeros", color='red')
plt.scatter(x_ones_x, x_ones_y, label="Ones", color='blue')

predicted_ones_x = x_np[y_pred_np.flatten() == 1][:, 0]
predicted_ones_y = x_np[y_pred_np.flatten() == 1][:, 1]
predicted_zeros_x = x_np[y_pred_np.flatten() == 0][:, 0]
predicted_zeros_y = x_np[y_pred_np.flatten() == 0][:, 1]

plt.scatter(predicted_ones_x, predicted_ones_y, label="Model Preidcted One", marker='x', color='purple', s=125)
plt.scatter(predicted_zeros_x, predicted_zeros_y, label="Model Predicted Zero", marker='x', color='yellow', s=125)

plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.show()

sess.close()
