from player import Player


class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()

    # member methods
    def welcome(self):
        print('no more of that boring old rock paper scissors. lets take it up a notch with the new and improved ROCK PAPER SCISSORS SPOCK!')

    def rules(self):
        print('How to play:')
        print('this updated version the the old classic game is pretty similar just with a few new gesture options to throw down.')
        print('Rock crushes Scissors')
        print('Scissors cuts Paper')
        print('Paper covers Rock')
        print('Rock crushes Lizard')
        print('Lizard poisons Spock')
        print('Spock smashes Scissors')
        print('Scissors decapitates Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rock')

    def player_selection(self):
