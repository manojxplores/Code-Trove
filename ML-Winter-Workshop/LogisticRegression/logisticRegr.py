import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv('ML-Winter-Workshop/Logistic Regression/ds1_train.csv')
print(df.head())

# Extract features and labels
x_train = df[['x_1', 'x_2']].values
y_train = df['y'].values
class1_data = df['x_1']
class2_data = df['x_2']

# Initialize weights and bias
num_features = x_train.shape[1]
weights = np.zeros(num_features)
bias = 0

# Print the number of features and initial weights shape
print(f'Number of features: {num_features}\nInitial weights shape: {weights.shape}')

# Set hyperparameters
learning_rate = 0.001
num_iterations = 100000

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Gradient Descent
loss_history = []

for i in range(num_iterations):
    # Forward pass
    z = np.dot(x_train, weights) + bias
    predictions = sigmoid(z)
    dl_db = 0
    # Backward pass
    dl_dw = np.dot(x_train.T, (predictions - y_train)) / x_train.shape[0]
    dl_db += (predictions - y_train) / x_train.shape[0]
    # Update weights and bias
    weights -= learning_rate * dl_dw
    bias -= learning_rate * dl_db

    # Calculate and store the loss
    loss = -np.sum(y_train * np.log(predictions) + (1 - y_train) * np.log(1 - predictions)) / x_train.shape[0]
    loss_history.append(loss)

    # Print the loss every 1000 iterations
    if i % 1000 == 0:
        print(f'Iteration {i}; Loss = {loss}')

# Plot the loss over iterations
plt.plot(loss_history)
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.title('Loss over Iterations')
plt.show()

# Plot the decision boundary
x_boundary = np.linspace(min(x_train[:, 0]), max(x_train[:, 0]), 100)
y_boundary = -(bias + weights[0] * x_boundary) / weights[1]
#plotting: w[0]+w[1]*x + w[2]*y=0

# Plot the data points
plt.scatter(class1_data[:, 0], class1_data[:, 1], label='Class 1', marker='o')
plt.scatter(class2_data[:, 0], class2_data[:, 1], label='Class 2', marker='x')

# Plot the decision boundary
plt.plot(x_boundary, y_boundary, label='Decision Boundary', color='red')

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.title('Logistic Regression Decision Boundary')
plt.show()
