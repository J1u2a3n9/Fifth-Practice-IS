from player import Player
from game import Game
from board import Board
from agents.console_input_agent import ConsoleInputAgent
from agents.min_max_agent import MinMaxAgent
from agents.min_max_cutt_off_agent import MinMaxCuttOff
from agents.min_max_alphabeta_prunning_agent import MinMaxCuttAlphaBetaPrunning

AGENTS = [
    ("Human", ConsoleInputAgent),
    ("Min Max Agent", MinMaxAgent),
    ("Min Max Alpha Beta Prunning", MinMaxCuttAlphaBetaPrunning),
    ("Min Max Cut Off", MinMaxCuttOff)
]

RESULTS = [
    ["Draws", 0],
    ["X wins", 0],
    ["O wins", 0]
]


def _pick_agent(player):
    def _try_pick():
        try:
            list_of_agents = "\n".join(
                map(lambda x: "\t{} - {}".format(x[0], x[1][0]),
                    enumerate(AGENTS)))
            agent = int(
                input("Available agents: \n{}\nPick an agent [0-{}]: ".format(
                    list_of_agents, len(AGENTS) - 1)))
            return agent
        except ValueError:
            return None
    agent = _try_pick()
    while agent is None:
        print("Incorect selection, try again.")
        agent = _try_pick()
    return AGENTS[agent][1](player)


def main():
    print("Choosing player X...")
    player_x = _pick_agent(Player.X)
    print("Choosing player O...")
    player_o = _pick_agent(Player.O)
    size = int(input("Select size of the board >= 3: "))
    to_win = size
    play = "y"
    games = 0
    while play == "y":
        game_board = None
        game = Game(player_x, player_o, size, to_win, game_board)
        res = game.play()
        games += 1
        RESULTS[res + 1][1] += 1
        for line in RESULTS:
            print(*line)
        print("")
        result=0.0
        result_2=0.0
        if player_x._num_moves != 0:
            result=player_x._time/player_x._num_moves
        if player_o._num_moves != 0:
            result_2=player_o._time/player_o._num_moves  
        print("X  runtime: ",result)
        print("O  runtime: ",result_2)
        print("States visited X", player_x.states_visited)
        print("States visited O", player_o.states_visited)
        play = input("Play again? y/[n]: ")



if __name__ == "__main__":
    main()
