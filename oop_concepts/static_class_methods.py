class Dog:
    dogs = []

    def __init__(self, name):
        self.name = name 
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        '''bark n time'''
        for _ in range(n):
            print(Bark)

tim = Dog("tim")
jim = Dog ("jim")

import private_public_classes
from private_public_classes import NotPrivate

test = NotPrivate("tim")
test.display()