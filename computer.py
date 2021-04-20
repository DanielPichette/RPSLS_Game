import random
from player import Player


class Computer(Player):
    super().__init__()

    def select(self):
        computer_selection = random.choice(self.gestures)
        return computer_selection

    def create_player(self):
        self.name = 'computer player'
        return self.name
