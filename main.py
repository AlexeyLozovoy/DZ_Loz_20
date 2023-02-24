from model import Game
from view import ConsoleView
from controller import GameController

game = Game()
view = ConsoleView()
controller = GameController(game, view)
controller.run()
