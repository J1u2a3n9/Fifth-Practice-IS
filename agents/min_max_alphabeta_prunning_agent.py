from copy import deepcopy
from numpy import inf
import timeit
from agents.base_agent import Agent, Move
from player import other_player


class MinMaxCuttAlphaBetaPrunning(Agent):
    def __init__(self, player):
        super().__init__(player)
        self._u_table = {}
        self._h_table = {}
        self._states_visited = 0

    def next_move(self, board):
        start = timeit.default_timer()
        self._h_table = {}
        move = self.abminimax(board, max(9 - board._num_to_win, 3), self._player, -inf, inf)[0] 
        end = timeit.default_timer()
        self._time += (end-start)
        self._num_moves += 1
        return move

    def abminimax(self, board, depth, player, alpha, beta):
        hash = board.hash
        if hash in self._u_table:
            return self._u_table[hash]
        self._states_visited += 1       
        valid_moves = self._valid_moves(board, player)
        #terminal cases
        if board.winner is not None:
            return -1, 1 if board.winner == self._player else -1, -1
        if len(valid_moves) == 0 or depth == 0:
            return -1, 0
        #default result that keeps track of the best so far
        if player == self._player:
            best_result = -1, -inf
        else:
            best_result = -1, inf
        #sorts the dictionary in descending order. moves with the highest 
        sorted_valid_moves = sorted(valid_moves, key = lambda i: i[1], reverse = True)
        #analyze each move
        for move in sorted_valid_moves:
            board.set_cell(move.player, move.row, move.col)
            result = move, self.abminimax(board, depth-1, other_player(player), alpha, beta)[1]
            board.set_cell(-1, move.row, move.col)
            if player == self._player:
                best_result = max(best_result, result, key = lambda i: i[1])
                alpha = max(alpha, best_result[1])
                if alpha >= beta:
                    break
            else:
                best_result = min(best_result, result, key = lambda i: i[1])
                beta = min(beta, best_result[1])
                if alpha >= beta:
                    break
        self._u_table[hash] = best_result
        return best_result

    #overriden method from base_agent to account for player
    def _valid_moves(self, board, player):
        valid_moves = []
        for i, j in board.empty_cells:
            valid_moves.append(Move(player, i, j))
        return valid_moves

   
