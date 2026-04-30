import numpy as np
X = np.load("features/features.npy")
y = np.load("features/labels.npy")
print(X.shape)
print(y.shape)
print(set(y))
