import matplotlib.pyplot as plt
import numpy as np
import random
import imageio


def random_walk(n):
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(0, n-1):
        value = random.choice([1, 2, 3, 4])  # 1 up, 2 right, 3 down, 4 left
        if value == 1:
            x[i+1] = x[i]
            y[i+1] = y[i] + 1
        elif value == 2:
            x[i+1] = x[i] + 1
            y[i+1] = y[i]
        elif value == 3:
            x[i+1] = x[i]
            y[i+1] = y[i] - 1
        else:
            x[i+1] = x[i] - 1
            y[i+1] = y[i]

    plt.plot(x,y)
    plt.show()

