import numpy as np
x = np.arange(12)
x = x.reshape(4,3)

# x = np.mean(x, axis=0)
x = x - np.mean(x, axis=0)
print(x)