import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([6,16,26, 36, 46, 56]).reshape((-1, 1))
y = np.array([4,23, 10, 12,22,35])

model = LinearRegression().fit(x, y)

r_sq = model.score(x, y)

print('intercept', model.intercept_)

print('slope', model.coef_)

y_predict = model.predict(x)
print('predicted re',  y_predict)