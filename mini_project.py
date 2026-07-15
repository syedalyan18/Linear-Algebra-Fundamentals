import numpy as np

np.random.seed(42)

X = 2 * np.random.rand(100,1)
y = 4 + 3*X + np.random.randn(100,1)

# Add bias column
x_b = np.c_[np.ones((100,1)), X]

theta = np.random.randn(2,1)

learning_rate = 0.1
iterations = 1000

def predict(X, theta):
    return np.dot(X, theta)

def descent_gradient(x, y, theta, learning_rate, iterations):
    m = len(y)

    for _ in range(iterations):
        gradients = (1/m) * np.dot(x.T, (np.dot(x, theta) - y))
        theta = theta - learning_rate * gradients

    return theta

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot)

optimized_theta = descent_gradient(x_b, y, theta, learning_rate, iterations)

y_pred = predict(x_b, optimized_theta)

mse = mean_squared_error(y, y_pred)
r2 = r_squared(y, y_pred)

print("Optimized Parameters (Theta):")
print(optimized_theta)

print("MSE:", mse)
print("R²:", r2)