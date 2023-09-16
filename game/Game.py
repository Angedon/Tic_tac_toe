class Game:
    def __init__(self, size, terminal):
        self.size = size
        self.terminal = terminal
        self.field = [['*' for j in range(self.size)] for i in range(self.size)]
        #self.terminal.choose_symbol()

    def set_bot(self, bot):
        self.bot = bot

    def print_arr(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.field[i][j], ' ', end='')
            print('\n')

    def get_count_of_free(self):
        k = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] == '*':
                    k += 1
        return k

    def end_of_game(self, board):
        for i in range(self.size):
            for j in range(self.size):
                counter_h = 0
                counter_v = 0
                for l in range(self.size):
                    if board[i][j] == board[i][l]:
                        counter_h += 1
                    if board[i][j] == board[l][j]:
                        counter_v += 1
                if board[i][j] == 'X' and (counter_h == self.size or counter_v == self.size):
                    return 'X'
                if board[i][j] == 'O' and (counter_h == self.size or counter_v == self.size):
                    return 'O'
        counter_1, counter_2 = 0, 0
        for i in range(self.size):
            if board[i][i] == board[self.size // 2][self.size // 2]:
                counter_1 += 1
            if board[self.size - 1 - i][i] == board[self.size // 2][self.size // 2]:
                counter_2 += 1
        if board[self.size // 2][self.size // 2] == 'X' and (
                counter_1 == self.size or counter_2 == self.size):
            return 'X'
        if board[self.size // 2][self.size // 2] == 'O' and (
                counter_1 == self.size or counter_2 == self.size):
            return 'O'
        if self.get_count_of_free() == 0:
            return 'Draw'
        else:
            #if (1):
            #return "Draw"
            #else:
            return None

    # (1) Проверка, что никто не может уже победить, исходя из того, что на каждой линии, вертикали, горизонтали, диагонали,
    # везде стоит как миниму один O и один X. Тогда вернуть True, иначе вернуть False.

    def print_result(self):
        if self.winner == self.terminal.player_symbol:
            print("Human win!")
        elif self.winner == self.terminal.bot_symbol:
            print("Bot win!")
        else:
            print("No one win!")

    def human_vs_bot(self):
        counter = 0
        player_turns, bot_turns = [], []
        self.winner = self.end_of_game(self.field)
        while counter != self.size ** 2 and self.winner == None:
            bot_turns.append(self.terminal.make_bot_move(player_turns, bot_turns))
            self.print_arr()
            self.winner = self.end_of_game(self.field)
            if self.winner != None:
                break
            player_turns.append(self.terminal.make_human_turn())

            self.winner = self.end_of_game(self.field)

        self.print_result()
