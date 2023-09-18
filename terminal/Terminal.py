
class Terminal:

    def set_field(self, field):
        self.field = field
        self.size = len(self.field)

    def set_bot(self, bot):
        self.bot = bot
        self.bot_symbol = bot.bot_symbol
        self.player_symbol = bot.player_symbol

    def make_bot_move(self, player_turns, bot_turns):
        i, j = self.bot.turn(bot_turns, player_turns)

        if (-1 < i < self.size) and (-1 < j < self.size):
            bot_turns.append((i, j))
            self.field[i][j] = self.bot_symbol
        return (i, j)

    def make_human_turn(self):
        x, y = input().split(' ')
        x, y = int(x), int(y)
        while self.field[x - 1][y - 1] != '*':
            print("Input again! This cell is not free!")
            x, y = input().split(' ')
            x, y = int(x), int(y)
        self.field[x - 1][y - 1] = self.player_symbol
        return (x-1, y-1)

    def print_horizontal(self):
        for i in range(2*self.size):
            print('-', end='')

    def print_arr(self):
        for i in range(self.size):
            #self.print_horizontal()
            for j in range(self.size):
                print(self.field[i][j], ' ', end='')
            print('\n')
        #self.print_horizontal()