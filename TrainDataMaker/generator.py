from abc import ABCMeta, abstractmethod
import typing
import numpy as np

Array2D = typing.NewType('Array2D', np.array)
Param = typing.NewType('Param', typing.Any)


class DataGenerator(metaclass=ABCMeta):
    '''
    implement
    ---
    def generate(self, param: typing.Any) -> Array2D:
    '''
    @abstractmethod
    def generate(self, param: typing.Any) -> Array2D:
        pass


class RandomParamGenerator(metaclass=ABCMeta):
    @abstractmethod
    def generate(self) -> Param:
        pass
