import random

class Bot:
    def __init__(self):
        self.choose_symbol("Choose your symbol: ")

    def choose_symbol(self, message):
        symbol = input(message)
        if symbol != 'X' and symbol != 'O':
            self.choose_symbol("Incorrect symbol, try again: ")
        else:
            self.player_symbol = symbol
            self.bot_symbol = 'O' if symbol == 'X' else 'X'

    def set_game(self, tic_tac_toe):
        self.tic_tac_toe = tic_tac_toe
        self.n = self.tic_tac_toe.size
        self.field = self.tic_tac_toe.field

    def is_terminal_node(self, board):
        winner = self.tic_tac_toe.end_of_game(board)
        if winner == self.bot_symbol:
            return (True, 1)
        elif winner == self.player_symbol:
            return (True, -1)
        elif winner == 'Draw':
            return (True, 0)

        return (False, 0)

    def get_current_field(self, my_turns, enemy_turns):
        arr = [['*' for j in range(self.tic_tac_toe.size)] for i in range(self.tic_tac_toe.size)]
        for turn in my_turns:
            arr[turn[0]][turn[1]] = self.bot_symbol
        for turn in enemy_turns:
            arr[turn[0]][turn[1]] = self.player_symbol
        return arr

    @staticmethod
    def get_free_cells(board):
        free_cells = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '*':
                    free_cells.append((i, j))
        return free_cells

    def min_max(self, depth, maximize_player, my_turns, enemy_turns):
        board = self.get_current_field(my_turns, enemy_turns)
        couple = self.is_terminal_node(board)
        if depth == 0 or couple[0]:
            return (couple[1], depth)

        if maximize_player:
            best_value = -10000000
            for pair in self.get_free_cells(board):
                my_turns_copy = my_turns.copy()
                my_turns_copy.append(pair)
                node = self.min_max(depth - 1, False, my_turns_copy, enemy_turns)
                best_value = max(node[0], best_value)

            return (best_value, depth)
        else:
            best_value = 100000000
            for pair in self.get_free_cells(board):
                enemy_turns_copy = enemy_turns.copy()
                enemy_turns_copy.append(pair)
                node = self.min_max(depth - 1, True, my_turns, enemy_turns_copy)
                best_value = min(node[0], best_value)

            return (best_value, depth)

    def count_of(self, board):
        k = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == self.bot_symbol:
                    k += 1
        return k

    def check_if_lose(self, board):
        for cell in self.get_free_cells(board):
            if board[cell[0]][cell[1]] == '*':
                board[cell[0]][cell[1]] = self.player_symbol
                if self.is_terminal_node(board)[1] == -1:
                    board[cell[0]][cell[1]] = '*'
                    return cell
                board[cell[0]][cell[1]] = '*'
        return (-1, -1)

    def check_if_win(self, board):
        for cell in self.get_free_cells(board):
            if board[cell[0]][cell[1]] == '*':
                board[cell[0]][cell[1]] = self.bot_symbol
                if self.is_terminal_node(board)[1] == 1:
                    board[cell[0]][cell[1]] = '*'
                    return cell
                board[cell[0]][cell[1]] = '*'
        return (-1, -1)

    def make_bot_move(self, player_turns, bot_turns):
        i, j = self.turn(bot_turns, player_turns)

        if (-1 < i < self.size) and (-1 < j < self.size):
            bot_turns.append((i, j))
            self.field[i][j] = self.bot_symbol
        return (i, j)

    def get_random_pair(self, my_turns, enemy_turns):
        x, y = random.randint(0, self.n-1), random.randint(0, self.n - 1)
        while (x, y) in my_turns or (x, y) in enemy_turns:
            x, y = random.randint(0, self.n - 1), random.randint(0, self.n - 1)
        return (x, y)

    def turn(self, my_turns, enemy_turns):
        board = self.get_current_field(my_turns, enemy_turns)
        self.size = len(board)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '*':
                    my_turns_copy = my_turns.copy()
                    my_turns_copy.append((i, j))
                    k, l = self.check_if_win(board)
                    if k != -1 and l != -1:
                        return (k, l)
                    k, l = self.check_if_lose(board)

                    if k != -1 and l != -1:
                        return (k, l)
                    #value = self.min_max(4, True, my_turns_copy, enemy_turns)
                    #if value[0] == 1:
                    #    k, l = i, j
                    #elif value[0] == 0:
                    #    m, n = i, j
        return self.get_random_pair(my_turns, enemy_turns)
        #if k == -1:
            #return (m, n)
        #else:
            #return (k, l)


