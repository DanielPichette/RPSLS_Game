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
        print('     HOW TO PLAY::')
        print('this updated version the the old classic game is pretty similar just with a few additions '
              'throw down.')
        print('     RULES:')
        print('-Rock crushes Scissors')
        print('-Scissors cuts Paper')
        print('-Paper covers Rock')
        print('-Rock crushes Lizard')
        print('-Lizard poisons Spock')
        print('-Spock smashes Scissors')
        print('-Scissors decapitates Lizard')
        print('-Lizard eats Paper')
        print('-Paper disproves Spock')
        print('-Spock vaporizes Rock')
        print("Now that you're all up to speed with the rules, lets start the game!")
        print('Lets start with best out of 3.')

    def rules_prompt(self):
        rule_prompt = input('Are you familiar with the rules?')
        if rule_prompt == 'yes':
            print('Fantastic!')
            print('Lets start with best out of 3.')
        elif rule_prompt == 'no':
            self.rules()
        else:
            print('sorry that input is invalid. please print "yes"" or "no"')
            self.rules_prompt()

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
            self.select_player1()

    def select_player2(self):
        player2_prompt = input('is player two a computer player?')
        if player2_prompt == 'no':
            self.player2 = Human()
            return self.player2
        elif player2_prompt == 'yes':
            self.player2 = Computer()
            return self.player2
        else:
            print('sorry that input is invalid. please print "yes"" or "no"')
            self.select_player2()

    def rpsls_shoot(self):
        print(f'    {self.player1.name}s turn!')
        self.player1.select()
        print(f'    {self.player2.name}s turn!')
        self.player2.select()

    def selections(self):
        print('     SELECTIONS:')
        print(f'Player 1 ({self.player1.name}): {self.player1.chosen_gesture}')
        print(f'Player 2 ({self.player2.name}): {self.player2.chosen_gesture}')

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
        print('     CURRENT SCORE:')
        print(f'Player 1 ({self.player1.name}) score : {self.player1.score}')
        print(f'Player 2 ({self.player2.name}) score : {self.player2.score}')

    def final_score(self):
        print('     THE FINAL SCORE IS:')
        print(f'Player 1 ({self.player1.name}) score : {self.player1.score}')
        print(f'Player 2 ({self.player2.name}) score : {self.player2.score}')

    def best_of_3(self):
        while self.player1.score or self.player2.score < 2:
            self.rpsls_shoot()
            self.selections()
            self.determine_winner()
            self.current_score()
            if self.player1.score == 2:
                print('     WE HAVE A WINNER!')
                print(f'{self.player1.name} Wins!')
                self.final_score()
                print('     WELL PLAYED!')
                break
            elif self.player2.score == 2:
                print('     WE HAVE A WINNER!')
                print(f'{self.player2.name} Wins!')
                self.final_score()
                print('     WELL PLAYED!')
                break

    def end_game(self):
        if self.player1.score > self.player2.score:
            print(f'Player 1 ({self.player1.name}) Is the Winner!')
        elif self.player1.score < self.player2.score:
            print(f'Player 2 ({self.player2.name}) Is the Winner!')
        elif self.player1.score == self.player2.score:
            print("It's a Tie!")

    def continue_playing_prompt(self):
        continue_game = input('Would you like to continue playing?')
        if continue_game == 'yes':
            self.rpsls_shoot()
            self.selections()
            self.determine_winner()
            self.continue_playing_prompt()
        elif continue_game == 'no':
            self.end_game()
            self.final_score()
            print('Thanks for playing!')
        else:
            print("Sorry i didn't recognize that input. please make sure your input is 'yes' or 'no'")
            self.continue_playing_prompt()

    def run_game(self):
        self.welcome()
        self.rules_prompt()
        self.select_player1()
        self.select_player2()
        self.best_of_3()
        self.continue_playing_prompt()
