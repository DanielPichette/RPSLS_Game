from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()

    def select(self):
        print(self.gestures)
        selection_prompt = input('which of the gestures do you choose to throw down?')
        for option in self.gestures:
            if selection_prompt == option:
                self.chosen_gesture = selection_prompt
                return self.chosen_gesture
        else:
            print("Sorry i didn't recognize that input. please make sure your input matches one of the gesture "
                  "options listed")
            self.select()

    def create_player(self):
        self.name = input('what is the name of this player?')
        return self.name
