from pyfractions.operations import *


class Polynomial:
    def __init__(self, cooficients):
        self.cooficients = cooficients

    def print(self):
        return self.cooficients

    def divide(self, a):
        new_cooficients = [self.cooficients[0]]
        for i in range(1, len(self.cooficients)):
            new_cooficients.append(a * new_cooficients[-1] + self.cooficients[i])
        remainder = new_cooficients.pop()
        return new_cooficients, remainder


