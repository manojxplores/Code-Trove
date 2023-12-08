import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# importing the fashion mnist dataset
data_set = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data_set.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0

# building the model 

model = tf.keras.Sequential([tf.keras.layers.Flatten(input_shape = (28, 28)),
                             tf.keras.layers.Dense(128, activation = 'relu'),
                             tf.keras.layers.Dense(10)])

# compile the model
model.compile(optimizer = 'adam', loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
              metrics = ['accuracy'])

model.fit(train_images, train_labels, epochs = 20)

prob_model =tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = prob_model.predict(test_images)

