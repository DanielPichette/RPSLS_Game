class Player:
    def __init__(self):
        self.gestures = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        self.name = 'player'
        self.chosen_gesture = self.select()
        self.score = 0

        # member methods

    def select(self):
        pass
