# from player import Player
from human import Human
from computer import Computer


class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None

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

    def print_player1(self):
        print('player 1: ' + self.player1.name)

    def print_player2(self):
        print('player 2: ' + self.player2.name)

    def select_player1(self):
        player1_prompt = input('is player 1 a computer player?')
        if player1_prompt == 'no':
            self.player1 = Human()
            return self.player1
        elif player1_prompt == 'yes':
            self.player1 = Computer()
            return self.player1
        else:
            print('sorry that input is invalid. please print "yes"" or "no"')

    def select_player2(self):
        player2_prompt = input('is player two a computer player?')
        if player2_prompt == 'no':
            self.player2 = Human()
            return self.player2
        elif player2_prompt == 'yes':
            self.player2 = Computer()
            return self.player2

    def rpsls_shoot(self):
        print(self.player1.name)
        self.player1.select()
        print(self.player2.name)
        self.player2.select()

    def selections(self):
        print('selections:')
        print(self.player1.name + ':' + self.player1.chosen_gesture)
        print(self.player2.name + ':' + self.player2.chosen_gesture)

    def determine_winner(self):
        # tie
        if self.player1.chosen_gesture == self.player2.chosen_gesture:
            print('Its a tie!')
        # rock and scissors
        elif self.player1.chosen_gesture == 'rock' and self.player2.chosen_gesture == 'scissors':
            self.player1.score += 1
            print('Rock crushes scissors!')
            print('player 1:' + self.player1.name + ' wins this round!')
            return self.player1.score
        elif self.player1.chosen_gesture == 'scissors' and self.player2.chosen_gesture == 'rock':
            self.player2.score += 1
            print('Rock crushes scissors!')
            print('player 2:' + self.player2.name + ' wins this round!')
            return self.player2.score
        # scissors and paper
        elif self.player1.chosen_gesture == 'scissors' and self.player2.chosen_gesture == 'paper':
            self.player1.score += 1
            print('scissors cut paper!')
            print('player 1:' + self.player1.name + ' wins this round!')
            return self.player1.score
        elif self.player1.chosen_gesture == 'paper' and self.player2.chosen_gesture == 'scissors':
            self.player2.score += 1
            print('scissors cut paper!')
            print('player 2:' + self.player2.name + ' wins this round!')
            return self.player2.score
        # paper and rock
        elif self.player1.chosen_gesture == 'paper' and self.player2.chosen_gesture == 'rock':
            self.player1.score += 1
            print('Paper covers rock!')
            print('player 1:' + self.player1.name + ' wins this round!')
            return self.player1.score
        elif self.player1.chosen_gesture == 'rock' and self.player2.chosen_gesture == 'paper':
            self.player2.score += 1
            print('Paper covers rock!')
            print('player 2:' + self.player2.name + ' wins this round!')
            return self.player2.score
        # rock and lizard
        elif self.player1.chosen_gesture == 'rock' and self.player2.chosen_gesture == 'lizard':
            self.player1.score += 1
            print('Rock crushes lizard!')
            print('player 1:' + self.player1.name + ' wins this round!')
            return self.player1.score
        elif self.player1.chosen_gesture == 'lizard' and self.player2.chosen_gesture == 'rock':
            self.player2.score += 1
            print('Rock crushes lizard!')
            print('player 2:' + self.player2.name + ' wins this round!')
            return self.player2.score
        # lizard and spock
        elif self.player1.chosen_gesture == 'lizard' and self.player2.chosen_gesture == 'spock':
            self.player1.score += 1
            print('Lizard poisons Spock!')
            print('player 1:' + self.player1.name + ' wins this round!')
            return self.player1.score
        elif self.player1.chosen_gesture == 'spock' and self.player2.chosen_gesture == 'lizard':
            self.player2.score += 1
            print('Lizard poisons Spock!')
            print('player 2:' + self.player2.name + ' wins this round!')
            return self.player2.score
        # spock scissors
        elif self.player1.chosen_gesture == 'spock' and self.player2.chosen_gesture == 'scissors':
            self.player1.score += 1
            print('Spock smashes scissors!')
            print('player 1:' + self.player1.name + ' wins this round!')
            return self.player1.score
        elif self.player1.chosen_gesture == 'scissors' and self.player2.chosen_gesture == 'spock':
            self.player2.score += 1
            print('Spock smashes scissors!')
            print('player 2:' + self.player2.name + ' wins this round!')
            return self.player2.score
        # scissors and lizard
        elif self.player1.chosen_gesture == 'scissors' and self.player2.chosen_gesture == 'lizard':
            self.player1.score += 1
            print('Scissors decapitates lizard!')
            print('player 1:' + self.player1.name + ' wins this round!')
            return self.player1.score
        elif self.player1.chosen_gesture == 'lizard' and self.player2.chosen_gesture == 'scissors':
            self.player2.score += 1
            print('Scissors decapitates lizard!')
            print('player 2:' + self.player2.name + ' wins this round!')
            return self.player2.score
        # lizard and paper
        elif self.player1.chosen_gesture == 'lizard' and self.player2.chosen_gesture == 'paper':
            self.player1.score += 1
            print('Lizard eats paper!')
            print('player 1:' + self.player1.name + ' wins this round!')
            return self.player1.score
        elif self.player1.chosen_gesture == 'paper' and self.player2.chosen_gesture == 'lizard':
            self.player2.score += 1
            print('Lizard eats paper!')
            print('player 2:' + self.player2.name + ' wins this round!')
            return self.player2.score
        # paper and spock
        elif self.player1.chosen_gesture == 'paper' and self.player2.chosen_gesture == 'spock':
            self.player1.score += 1
            print('Paper disproves Spock!')
            print('player 1:' + self.player1.name + ' wins this round!')
            return self.player1.score
        elif self.player1.chosen_gesture == 'spock' and self.player2.chosen_gesture == 'paper':
            self.player2.score += 1
            print('Paper disproves Spock!')
            print('player 2:' + self.player2.name + ' wins this round!')
            return self.player2.score
        # spock and rock
        elif self.player1.chosen_gesture == 'spock' and self.player2.chosen_gesture == 'rock':
            self.player1.score += 1
            print('Spock vaporizes rock!')
            print('player 1:' + self.player1.name + ' wins this round!')
            return self.player1.score
        elif self.player1.chosen_gesture == 'rock' and self.player2.chosen_gesture == 'spock':
            self.player2.score += 1
            print('Spock vaporizes rock!')
            print('player 2:' + self.player2.name + ' wins this round!')
            return self.player2.score

    def current_score(self):
        print('current Score')
        print(f'Player 1 ({self.player1.name}) score : {self.player1.score}')
        print(f'Player 2 ({self.player2.name}) score : {self.player2.score}')

    def final_score(self):
        print('The final score is:')
        print(f'Player 1 ({self.player1.name}) score : {self.player1.score}')
        print(f'Player 2 ({self.player2.name}) score : {self.player2.score}')

    def best_of_3(self):
        while self.player1.score or self.player2.score < 3:
            self.rpsls_shoot()
            self.selections()
            self.determine_winner()
            self.current_score()
        if self.player1.score == 3:
            print('WE HAVE A WINNER!')
            print(f'{self.player1} Wins!')
            self.final_score()
        elif self.player2.score == 3:
            print('WE HAVE A WINNER!')
            print(f'{self.player2} Wins!')
            self.final_score()
