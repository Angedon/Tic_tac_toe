from bot.Bot import Bot
from game.Game import Game
from gui.Gui import Gui
from terminal.Terminal import Terminal

N = 2

def play_game():
    terminal = Terminal()
    game = Game(N, terminal)

    bot = Bot(game)

    terminal.set_bot(bot)
    terminal.set_field(game.field)
    game.set_bot(bot)
    game.human_vs_bot()

def gu():
    terminal = Terminal()
    game = Game(N, terminal)
    bot = Bot(game)
    game.set_bot(bot)
    directory = r'C:\\Users\\Gleb1\\Downloads\\'
    gui = Gui(N, 500, 500, directory + 'crest1.png', directory + 'zero1.png', bot)
    gui.draw()

play_game()


