import random
import matplotlib.pyplot as plt
import os
import imageio
import natsort
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
    elif direction == 4:
        x2 = xi - 1
        y2 = yi
    return x2, y2

def random_walk_gif(n_steps, path_to_images, path_to_gif):
    """ Make a gif of randomly walking agent in four directions.
        :param n_steps: Amount of steps.
        :param path_to_images: Path to images of which gif will be created.
        :param path_to_gif: Path to the future gif.
        """
    X = []
    Y = []
    x0 = 0
    y0 = 0
    if n_steps > 0:
        for i in range(0, n_steps):
            x, y = move_one_step(x0, y0)
            X.append(x)
            Y.append(y)
            x0 = x
            y0 = y
            plt.plot(X,Y)
            plt.axis([-n_steps / 4, n_steps / 4, -n_steps / 4, n_steps / 4])
            plt.savefig('krok' + str(i) + '.png')

        images = []
        if os.path.isdir(path_to_images):
            if not os.path.isdir(path_to_gif):
                im = natsort.natsorted(os.listdir(path_to_images))
                for filename in im:
                    if filename.endswith('.png'):
                        file_paths = os.path.join(path_to_images, filename)
                        images.append(imageio.imread(file_paths))
                imageio.mimsave(path_to_gif, images, duration = 0.2)
            else:
                print("Given path to gif already exists.")
        else:
            print("Given path to images does not exists.")
    else:
        print("Amount of steps should be greater than 0")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make a gif of randomly walking agent in four directions.")
    parser.add_argument('-n_steps', type=int, help="Amount of agent's steps.")
    parser.add_argument('-path_to_images', type=str, help="Path to images of which gif will be created.")
    parser.add_argument('-path_to_gif', type=str, help="Path to the future gif")
    args = parser.parse_args()
    random_walk_gif(args.n_steps, args.path_to_images, args.path_to_gif)