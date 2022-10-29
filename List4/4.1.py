import argparse
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def model(y,T, Q, w, A):
    """ Solve equation of motion of a mathematical pendulum.
    :param y: ???
    :param T: ???
    :param Q: ???
    :param w: ???
    :param A: ???
    :return: ???
    """
    return (y[1], -(1/Q)*y[1] - np.sin(y[0]) + A * np.cos(w*T))


def visualisation(th, v, Q, w, A):
    """ Show visualisation of motion of a mathematical pendulum.
    :param th: Initial pendulum's angle.
    :param v: Initial velocity.
    :param Q: ???
    :param w: ???
    :param A: ???
    """
    y0 = [th, v]
    T = np.linspace(0,30,200)
    sol = odeint(model, y0, T, args=(Q,w,A))

    plt.plot(T,sol[:,0], 'b', label='theta(t)')
    plt.plot(T,sol[:,1], 'g', label='omega(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Show visualisation of motion of a mathematical pendulum")
    parser.add_argument('-Q', type=float, help="???")
    parser.add_argument('-w', type=str, help="???")
    parser.add_argument('-A', type=float, help="???")
    parser.add_argument('-v', type=float, help="Initial pendulum's velocity.")
    parser.add_argument('-th', type=float, help="Initial pendulum's angle.")

    args = parser.parse_args()

    Q = args.Q
    w = eval(args.w)
    A = args.A
    v = args.v
    th = args.th

    visualisation(th, v, Q, w, A)
