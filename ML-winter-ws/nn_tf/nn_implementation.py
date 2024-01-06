# load a data set
# build a nn model
# Train the model 
# make predictions

import tensorflow as tf
import pandas as pd
import numpy as np
# print(tf.__version__)

df = pd.read_csv('nn_tf/ds1_train.csv')
df_test = pd.read_csv('nn_tf/ds1_test.csv')

x_test = df_test[['x_1', 'x_2']]
y_test = df_test['y']


x_train = df[['x_1', 'x_2']]
y_train = df['y']

print(x_train.head)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(5, activation = 'sigmoid'),
    tf.keras.layers.Dense(3, activation = 'sigmoid'),
    tf.keras.layers.Dense(1, activation = 'sigmoid')
    ])

model.compile(loss = tf.keras.losses.BinaryCrossentropy(), metrics = ['accuracy'], optimizer = 'adam')

model.fit(x_train, y_train, epochs = 1000)

model.evaluate(x_test, y_test, verbose = 2)

