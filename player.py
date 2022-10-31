import random

# This class is used to play the game
class HumanPlayer():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        legal_move = False

        while(not legal_move):
            position = int(input('Enter your move (0 - 8) : '))
            print()

            if position not in game.legal_moves():
                print('That is not a legal move ! ')
                print()
            else: 
                legal_move = True

        return position

# This class is a computer player that plays random moves
class RandomComputer():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        position = random.choice(game.legal_moves())
        return position

# This class is a smart player that uses a minimax algorithm to play optimally
# The smart computer never loses, he only wins or ties
class SmartComputer():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        # If the board is completely open, start in the middle
        if len(game.legal_moves()) == 9:
            position = 4
        else:
            position = self.minimax(game, self.letter, 0)['position']
        return position

    def minimax(self, game, player, depth):
        # game : current game's board
        # player : player currently minimizing or maximizing
        # depth : current depth of the minimax, goes to a maximum of 9 (number of squares)

        depth += 1
        max_player = self.letter  # The current instance (player who started the algo) is always maximizing
        other_player = 'O' if player == 'X' else 'X'

        # Checks if last turn was a win or game is over
        # We add the depth component to differentiate long games and short games
        if game.winner == other_player:
            if other_player == max_player:
                return {'position': None, 'score': 10 - depth} # Maximizing player won, so we give a positive score and penalize long games
            else:
                return{'position' : None, 'score': depth - 10} # Minimizing player won, so we give a negative score and penalize long games

        elif  game.num_empty_squares() == 0:
            return {'position': None, 'score': 0} # Tie

        if player == max_player:
            outcome = {'position': None, 'score': -100}
        else:
            outcome = {'position': None, 'score': 100}

        # Checks all possible moves and gives the best one (min or max score)
        for legal_move in game.legal_moves():
            game.push_move(legal_move, player)
            next_node = self.minimax(game, other_player, depth) # Simulates next player's turn, and recurses through the whole game

            game.board[legal_move] = ' ' # Remove last move
            game.winner = None
            next_node['position'] = legal_move

            if player == max_player:
                if next_node['score'] > outcome['score']:
                    outcome = next_node
            else:
                if next_node['score'] < outcome['score']:
                    outcome = next_node
        return outcome

            



        





        

