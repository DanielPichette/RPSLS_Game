import random
from player import Player


class Computer(Player):
    def __init__(self):
        super().__init__()

    def select(self):
        self.chosen_gesture = random.choice(self.gestures)
        return self.chosen_gesture

    def create_player(self):
        self.name = 'computer player'
        return self.name
