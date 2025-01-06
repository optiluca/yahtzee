"""
iterators.py

Some useful iterators
"""
import functools
import itertools as it
from payoffs import PAYOFF_LS

def _rec_dice_state_iter(vec):

    if len(vec) == 1:
        yield vec
    else:
        while vec[0] >= 0:
            for suffix in _rec_dice_state_iter(vec[1:]): 
                yield vec[:1] + suffix 
            vec[0] -= 1
            vec[1] += 1

"""
Iterate through unique dice states.
Iterator was surprisingly slow - since we make the same calls over and over, just cache this.  It's not that much memory anyway.
"""
@functools.lru_cache
def dice_state_iter(n_dice, n_sides):

    dice_states = []

    vec = [n_dice] + [0]*(n_sides-1)

    for vec in _rec_dice_state_iter(vec):
        dice_states.append(tuple(vec))

    return dice_states
       

"""
Iterate through the possible "sub-states" of 
a dice state. I.e., the states obtained by
removing dice from a state.
""" 
def dice_substate_iter(dice_state):

    for substate in it.product(*[range(count+1) for count in dice_state]):
        yield substate


"""
Iterate through possible game states -- i.e.,
the possible combinations of filled/empty 
column entries.
"""
def game_state_iter():
    n_items_to_tick = len(PAYOFF_LS)
    for r in range(n_items_to_tick+1):
        for idx_tuple in it.combinations(range(n_items_to_tick), r):
            state = [True]*n_items_to_tick
            for idx in idx_tuple:
                state[idx] = False
            yield tuple(state)

"""
Given a game state, iterate through the 
available "payoff" actions
"""
def payoff_action_iter(game_state):

    for idx, box in enumerate(game_state):
        if box == False:
            yield idx



"""
Iterate through the "turn" states 
(i.e., all possible dice states for the three possible rolls) 
"""
def turn_state_iter():
    for roll in range(3, 0, -1):
        for dice_state in dice_state_iter(5,6):
            yield (roll, dice_state)



