import random
import math


class Vector:
    """ A class used to represent the vector as a list.
    """

    def __init__(self, n: int = 3):
        """Initialise an empty vector and determine its future dimension.
        :param n: dimension of the vector
        """
        if n <= 0:
            raise ValueError
        else:
            self.n = n
            self.elements = []

    def random_values(self):
        """ Generate random elements of the vector.
        """
        self.elements = (random.sample(range(-50, 50), self.n))

    def from_list(self, list0: list):
        """ Load vector's elements from the given list of integers.
        :param list0: List of desired vector's elements.
        """
        for i in range(0, len(list0)):
            if type(list0[i]) != int:
                raise ValueError
        if len(list0) != self.n:
            raise ValueError
        else:
            self.elements = list0

    def __add__(self, other):
        if self.n != other.n:
            raise ValueError
        else:
            vector = Vector()
            for i in range(0, self.n):
                vector.elements.append(self.elements[i] + other.elements[i])
        return vector.elements

    def __sub__(self, other):
        if self.n != other.n:
            raise ValueError
        else:
            vector = Vector()
            for i in range(0, self.n):
                vector.elements.append(self.elements[i] - other.elements[i])
        return vector.elements

    def __rmul__(self, number: float):
        """ Multiply the vector by scalar.
        :param number: A scalar.
        :return: scalar * vector
        """
        vector = Vector()
        for i in range(0, self.n):
            vector.elements.append(number * self.elements[i])
        return vector.elements

    def __mul__(self, number: float):
        """ Multiply the vector by scalar.
        :param number: A scalar.
        :return: vector * scalar
        """
        vector = Vector()
        for i in range(0, self.n):
            vector.elements.append(number * self.elements[i])
        return vector.elements

    def vec_len(self):
        """ Count the length of the vector.
        :return: (float) Length of the vector.
        """
        if len(self.elements) == 0:
            raise ValueError
        else:
            return math.sqrt(sum(i ** 2 for i in self.elements))

    def elem_sum(self):
        """ Add all vector's elements.
        :return: (int) Sum of the vector's elements.
        """
        if len(self.elements) == 0:
            return 0
        else:
            return sum(i for i in self.elements)

    def scalar_prod(self, other):
        """ Count the scalar product of two vectors.
        :param other: Another vector from class Vector.
        :return: (int) The scalar product of two vectors
        """
        list3 = []
        if self.n != other.n:
            raise ValueError
        elif len(self.elements) == 0 or len(other.elements) == 0:
            return 0
        else:
            for i in range(0, self.n):
                list3.append(self.elements[i] * other.elements[i])
        return sum(list3)

    def __str__(self):
        return str(self.elements)

    def __getitem__(self, index):
        if type(index) != int:
            raise ValueError
        elif index < 0 and abs(index) > self.n:
            raise ValueError
        elif index >= 0 and index >= self.n:
            raise ValueError
        else:
            return self.elements[index]

    def __contains__(self, item):
        if type(item) != int:
            raise ValueError
        elif item in self.elements:
            return True
        else:
            return False
