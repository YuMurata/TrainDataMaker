import typing
from .player import Player
from abc import ABCMeta, abstractmethod


class DistanceMeasurer(metaclass=ABCMeta):
    '''
    implement
    ---
    def measure(self, paramA: typing.Any, paramB: typing.Any) -> float

    paramA == paramB -> 0
    ret >= 0
    '''

    @abstractmethod
    def measure(self, paramA: typing.Any, paramB: typing.Any) -> float:
        pass


class Evaluator:
    def __init__(self, scored_player_list: typing.List[Player],
                 measurer: DistanceMeasurer):
        self.scored_player_list = scored_player_list
        self.sum_score = sum(
            [player.score for player in self.scored_player_list])
        self.measurer = measurer

    def evaluate(self, param):
        epsilon = 1
        return sum([player.score /
                    (self.measurer.measure(param, player.param) + epsilon)
                    for player in self.scored_player_list])/self.sum_score
