from player import Player


class Human(Player):
    super().__init__()

    def select(self):
        print(self.gestures)
        selection_prompt = input('which of the gestures do you choose to throw down?')
        for option in self.gestures:
            if selection_prompt == option:
                selection = selection_prompt
                return selection
            elif selection_prompt != option:
                selection_prompt = input(
                    'Sorry that input is invalid. please make sure your input matches an option on the list given. ('
                    'case sensitive)')
                player_selection = selection_prompt
                return player_selection
