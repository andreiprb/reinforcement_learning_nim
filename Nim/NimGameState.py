from Nim.NimLogic import NimLogic


class NimGameState:
    def __init__(self, initial, misere):
        self.piles = initial.copy()
        self.player = 0
        self.winner = None
        self.misere = misere

    def copy(self):
        new_state = NimGameState(self.piles, self.misere)
        new_state.player = self.player
        new_state.winner = self.winner
        return new_state

    def apply_move(self, action):
        pile, count = action
        new_state = self.copy()

        if self.winner is not None:
            raise Exception("Game already won")
        elif pile < 0 or pile >= len(self.piles):
            raise Exception("Invalid pile")
        elif count < 1 or count > self.piles[pile]:
            raise Exception("Invalid number of objects")

        new_state.piles[pile] -= count
        new_state.player = NimLogic.other_player(self.player)

        if all(pile == 0 for pile in new_state.piles):
            if new_state.misere:
                new_state.winner = new_state.player
            else:
                new_state.winner = self.player

        return new_state