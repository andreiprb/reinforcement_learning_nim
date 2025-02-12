from agents.QLearningAgent import QLearningAgent
from agents.AlphaZeroAgent import AlphaZeroAgent
from agents.MinimaxAgent import MinimaxAgent

from nim.NimGameState import NimGameState
from nim.NimLogic import NimLogic


AGENT = AlphaZeroAgent


class Nim:
    def __init__(self, initial=[1, 3, 5, 7]):
        self.state = NimGameState(initial)

    @property
    def piles(self):
        return self.state.piles

    @property
    def player(self):
        return self.state.player

    @property
    def winner(self):
        return self.state.winner

    def move(self, action):
        self.state = self.state.apply_move(action)


def train():
    player = AGENT()

    if AGENT is MinimaxAgent:
        print("Playing versus Minimax agent")
        return player

    player.train()
    return player