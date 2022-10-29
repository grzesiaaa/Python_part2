import random
import matplotlib.pyplot as plt
from PIL import Image
import argparse


def move_one_step(xi, yi):
    """ Move one step of length one on square grid in four random directions.
    :param xi: First coordinate of the point.
    :param yi: Second coordinate of the point.
    :return: New point's coordinates.
    """
    direction = random.choice([1, 2, 3, 4])
    if direction == 1:
        x2 = xi
        y2 = yi + 1
    elif direction == 2:
        x2 = xi + 1
        y2 = yi
    elif direction == 3:
        x2 = xi
        y2 = yi - 1
    else:
        x2 = xi - 1
        y2 = yi
    return x2, y2


def random_walk_gif(n_steps: int):
    """ Make a gif of randomly walking agent in four directions.
    :param n_steps: Amount of steps.
    """
    X = []
    Y = []
    x0 = 0
    y0 = 0
    images = []

    if n_steps > 0:
        for i in range(0, n_steps):
            x, y = move_one_step(x0, y0)
            X.append(x)
            Y.append(y)
            x0 = x
            y0 = y
            plt.plot(X, Y)
            plt.axis([-n_steps / 4, n_steps / 4, -n_steps / 4, n_steps / 4])
            plt.savefig('krok' + str(i) + '.png')
            images.append('krok' + str(i) + '.png')

        gif_images = []
        for filename in images:
            image = Image.open(filename)
            gif_images.append(image)

        gif_images[0].save('random_walk.gif',
                           save_all=True,
                           append_images=gif_images[1:],
                           duration=3,
                           loop=0)

    else:
        print("Amount of steps should be greater than 0")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make a gif of randomly walking agent in four directions.")
    parser.add_argument('-n_steps', type=int, help="Amount of agent's steps.")
    args = parser.parse_args()
    random_walk_gif(args.n_steps)
