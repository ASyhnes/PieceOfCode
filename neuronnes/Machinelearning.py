
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=100, n_features=2, centers=2, random_state=0)
y = y.reshape((y.shape[0], 1))

print('dimensions de X:', X.shape)
print('dimensions de y:', y.shape)

plt.scatter(X[:,0], X[:, 1], c=y, cmap='summer')
plt.show()

def initialisation(x):
        w = np.random.randn(x.shape[1], 1)
        b = np.random.randn(1)
        return (w,b)

w,b = initialisation(X)

#pour debug:
print(w.shape)
print(b.shape)
print(w)
print(b)

