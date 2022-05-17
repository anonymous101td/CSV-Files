import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('ggplot')

xs = np.array([10, 9, 2, 15, 10, 16, 11, 16], dtype=np.float64)
ys = np.array([95, 80, 10, 50, 45, 98, 38, 93], dtype=np.float64)

def best_fit_slope_and_intercept(xs, ys):
    x_mean = np.sum(xs) / np.size(xs)
    y_mean = np.sum(ys) / np.size(ys)

    xy_mean = (np.sum(xs * ys) / np.size(xs))

    x_mean_sq = x_mean * x_mean
    x_sq_mean = (np.sum(xs * xs) / np.size(xs))

    m = (((x_mean * y_mean) - xy_mean) /
         (x_mean_sq - x_sq_mean))

    b = (y_mean - (m * x_mean))

    return m, b

m, b = best_fit_slope_and_intercept(xs, ys)

#print(m, b)

regression_line = [(m * x) + b for x in xs]

predict_x = 20
predict_y = (m * predict_x) + b

plt.scatter(xs, ys, color='#003F72', label='data')
plt.scatter(predict_x, predict_y, color='g')
plt.plot(xs, regression_line, label='regression line')
plt.legend(loc=4)
plt.show()

print("Equation of best fit line:\n")
print("y =", format(m, '.3f'), "x +", format(b, '.3f'))