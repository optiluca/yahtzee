from os import path
import pickle as pkl
from yahtzee.solve import solve_game

WORKING_DIR = path.dirname(path.abspath(__file__))

if __name__=="__main__":

    game_state_values = solve_game()

    pkl.dump(game_state_values, open(path.join(WORKING_DIR, "game_state_values.pkl"), "wb"))

