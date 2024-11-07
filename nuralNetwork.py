# Import necessary libraries
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Example: XOR Problem (for simplicity)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input
y = np.array([[0], [1], [1], [0]])  # Output (XOR)

# Build a simple neural network
model = Sequential()
model.add(Dense(8, input_dim=2, activation='relu'))  # Hidden layer with 8 neurons
model.add(Dense(1, activation='sigmoid'))  # Output layer

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=1000, verbose=0)

# Make a prediction
prediction = model.predict(X)
print(prediction)
