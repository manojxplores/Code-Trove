import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

df = pd.read_csv('IRIS.csv')

X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

label_encoder = preprocessing.LabelEncoder()
y = label_encoder.fit_transform(df['species'])

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(15, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'], optimizer='Adam')

model.fit(x_train, y_train, epochs=500)

loss, accuracy = model.evaluate(x_test, y_test, verbose = 0)
print(f'loss {loss}')
print(f'accuracy{accuracy}')