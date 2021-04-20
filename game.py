from player import Player
from human import Human
from computer import Computer


class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()

    # member methods

    def welcome(self):
        print('no more of that boring old rock paper scissors. lets take it up a notch with the new and improved ROCK '
              'PAPER SCISSORS SPOCK!')

    def rules(self):
        print('How to play:')
        print('this updated version the the old classic game is pretty similar just with a few new gesture options to '
              'throw down.')
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

    def select_player1(self):
        player1_prompt = input('is player one a computer player?')
        if player1_prompt == 'no':
            self.player1 = Human.create_player()
            return self.player1
        elif player1_prompt == 'yes':
            self.player1 = Computer.create_player()
            return self.player1
        else:
            print('sorry that input is invalid. please print "yes"" or "no"')

    def select_player2(self):
        player2_prompt = input('is player two a computer player?')
        if player2_prompt == 'no':
            self.player2 = Human.create_player()
            return self.player2
        elif player2_prompt == 'yes':
            self.player2 = Computer.create_player()
            return self.player2
