'''
Python do not support Abstract Implicitly
We have to Import 'ABC' class and decorater 'abstractmethod' from 'abc' module
and use them accordingly as below
'''
from abc import ABC, abstractmethod


class Computer(ABC):

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class Laptop(Computer):
    def process(self):
        print('Its Running')


com = Laptop()
com.process()
# com.execute()  # Error
