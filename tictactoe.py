import math
from random import random

from player import HumanPlayer, RandomComputer, SmartComputer

class TicTacToe():
    def __init__(self):
        self.board = self.new_board()
        self.winner = None

    @staticmethod
    def new_board():
        return [' ' for i in range(9)]

    @staticmethod
    def position_to_square(position):
        # Transfroms a position (0 - 8) to a square[0 - 2][0 - 2]
        row = math.floor(position / 3)
        col = position - row*3
        square = [row, col]
        return square

    @staticmethod
    def square_to_position(square):
        # Transfroms a square[0 - 2][0 - 2] to a position (0 - 8)
        position = square[1] + square[0] * 3
        return position

    def print_board(self):
        for row in range(3):
            for col in range(3):
                position = TicTacToe.square_to_position([row, col])
                if col < 2:
                    print(' ' + str(self.board[position]) + ' |', end = '')
                if col == 2:
                    print(' ' + str(self.board[position]))
        print()
    
    @staticmethod
    def print_board_pos():
        # Prints boards positions [0 - 8] for UI purposes
        rowAdd = 0
        for row in range(3):
            for col in range(3):
                position = TicTacToe.square_to_position([row, col])
                if col < 2:
                    print(' ' + str(position) + ' |', end = '')
                if col == 2:
                    print(' ' + str(position))
            rowAdd += 3
        print()

    def push_move(self, position, letter):
        if self.board[position] == ' ':
            self.board[position] = letter
            if self.game_winner(position, letter):
                self.winner = letter
            return True

    def game_winner(self, position, letter):
        # Return True if a game has a winner after pushing a move
        square = TicTacToe.position_to_square(position)


        # Checks the row 
        row_num = square[0]
        row = self.board[row_num * 3 : ((row_num) + 1) * 3]

        if all(l == letter for l in row):
            return True

        # Checks the column
        col_num = square[1]
        col = [self.board[col_num + i * 3] for i in range(3)]    
        
        if all(l == letter for l in col):
            return True

        # Checks both diagonals
        first_diag = [self.board[i] for i in [0, 4, 8]]
        second_diag = [self.board[i] for i in [2, 4, 6]]

        if all(l == letter for l in first_diag) or all(l == letter for l in second_diag):
            return True
        
        return False

    def num_empty_squares(self):
        return self.board.count(' ')

    def legal_moves(self):
        legal_moves = []
        for i in range(len(self.board)):
            if(self.board[i] == ' '):
                legal_moves.append(i)

        return legal_moves


        

    def play(game, x_player, o_player, print_game):
        # game : current game's board
        # x_player : player who has the 'X' letter
        # o_player : player who has the 'O' letter
        # print_game : True if you want to print the game

        letter = 'X' # X always makes the first move

        if print_game:
                TicTacToe.print_board_pos()

        while(game.winner == None and game.num_empty_squares() != 0):
            if print_game:
                game.print_board()

            if letter == 'O':
                position = o_player.get_move(game)
            else:
                position = x_player.get_move(game)

            if game.push_move(position, letter):
                if print_game:
                    print(letter + ' makes a move...')
                    print()

                if game.winner:
                    if print_game: game.print_board()
                    # print(letter + ' wins !')
                    return letter

                if game.num_empty_squares() == 0:
                    if print_game: game.print_board()
                    # print('Tie !')
                    return 'Tie'

            letter = 'O' if letter == 'X' else 'X' # Switches turns
        

# This function generates results
def tester(TicTacToe, x_player, o_player, iterations):
    x_wincount = 0
    o_wincount = 0
    tie_count = 0
    for i in range(iterations):
        game = TicTacToe()
        result = TicTacToe.play(game, x_player, o_player, False)
        # print(str(i + 1))
        if(result == 'X'): x_wincount += 1
        elif(result == 'O'): o_wincount += 1
        else: tie_count += 1

    print('X wins : ' + str(x_wincount) + ' O wins : ' + str(o_wincount) + ' Ties : ' + str(tie_count))

if __name__ == '__main__':

    tester(TicTacToe, RandomComputer('X'), RandomComputer('O'), 10000)
    tester(TicTacToe, SmartComputer('X'), RandomComputer('O'), 10000)
    tester(TicTacToe, RandomComputer('X'), SmartComputer('O'), 10000)
    tester(TicTacToe, SmartComputer('X'), SmartComputer('O'), 10000)


