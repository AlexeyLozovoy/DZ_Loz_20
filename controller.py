class GameController:
    def __init__(self, game, view):
        self.game = game
        self.view = view

    def run(self):
        self.view.show_game(self.game.turn, self.game.player_score, self.game.computer_score)

        while True:
            user_input = self.view.get_input()

            if user_input == "1":
                self.game.roll_dice()
                self.view.show_game(self.game.turn, self.game.player_score, self.game.computer_score)

            elif user_input == "2":
                self.game.reset()
                self.view.show_game(self.game.turn, self.game.player_score, self.game.computer_score)

            elif user_input == "0":
                break

            else:
                self.view.show_invalid_input()

        self.view.show_winner(self.game.player_score, self.game.computer_score)
