import numpy as np
def gradient_descent(gradient, start, learn_rate, n_iter=50,tolerance=1e-06):
    vector = start
    for _ in range(n_iter):
        diff = -learn_rate * gradient(vector)
        if np.all(np.abs(diff) <= tolerance):
            break
        vector += diff
    return vector

# c=v-log(v)
print(gradient_descent(gradient=lambda v: 1 - 1/v, start=2.5, learn_rate=0.5,n_iter=50,tolerance=1e-06))