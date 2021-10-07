from agents.base_agent import Agent, Move
from player import player_names
import timeit



class ConsoleInputAgent(Agent):
    def __init__(self, player):
        super().__init__(player)

    def transform_to_number(self,letter):
        if letter=='A' or letter=='a':
            return 0
        if letter=='B' or letter=='b':
            return 1
        if letter=='C' or letter=='c':
            return 2
        if letter=='D' or letter=='d':
            return 3
        if letter=='E' or letter=='e':
            return 4
        if letter=='F' or letter=='f':
            return 5
        if letter=='G' or letter=='g':
            return 6

    def next_move(self, board):
        def _input_move():
            try:
                print("")
                print("{}'s next move".format(player_names[self._player]))
                col = self.transform_to_number(input("\tcol: "))
                row = int(input("\trow: "))-1
                print("")
                return Move(self._player, row, col)
            except ValueError:
                print("Row an col must be integers between 0 and {}".format(board.size))
        start = timeit.default_timer()
        move = _input_move()
        valid_moves = self._valid_moves(board)
        while move not in valid_moves:
            print("{} is not valid, try again.".format(move))
            print("Valid moves: " + str(valid_moves))
            move = _input_move()
        end = timeit.default_timer()
        self._time += (end-start)
        self._num_moves += 1
        return move
