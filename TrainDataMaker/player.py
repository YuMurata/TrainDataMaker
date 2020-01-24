import typing


class Player:
    def __init__(self, param: typing.Any, score: int):
        self.param = param
        self.score = score

    def to_dict(self):
        return {'score': self.score, 'param': self.param}
