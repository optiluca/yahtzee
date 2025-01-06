

def compute_payoff(action, dice_state):
    return PAYOFF_LS[action][1](dice_state)

def ones_payoff(dice_state):
    return 1.0*dice_state[0]

def twos_payoff(dice_state):
    return 2.0*dice_state[1]
   
def threes_payoff(dice_state):
    return 3.0*dice_state[2]

def fours_payoff(dice_state):
    return 4.0*dice_state[3]

def fives_payoff(dice_state):
    return 5.0*dice_state[4]

def sixes_payoff(dice_state):
    return 6.0*dice_state[5]

def one_pair_payoff(dice_state):
    score = 0.0

    for n_dice, v in reversed(list(zip(dice_state, range(1, 7)))):
        if n_dice >= 2.0:
            score = v * 2.0
            break

    return score

def two_pairs_payoff(dice_state):
    score = 0.0
    n_pairs = 0

    for n_dice, v in reversed(list(zip(dice_state, range(1, 7)))):
        if n_dice >= 2.0:
            score += v * 2.0
            n_pairs+=1
            if n_pairs == 2:
                break

    return score

def three_of_a_kind_payoff(dice_state):
    score = 0.0

    for n_dice, v in reversed(list(zip(dice_state, range(1,7)))):
        if n_dice >= 3.0:
            score = v * 3.0
            break
    
    return score

def four_of_a_kind_payoff(dice_state):
    score = 0.0

    for n_dice, v in reversed(list(zip(dice_state, range(1,7)))):
        if n_dice >= 4.0:
            score = v * 4.0
            break
    
    return score

def full_house_payoff(dice_state):
    score = 0.0
    found_3 = False
    found_2 = False
    for n_dice, v in reversed(list(zip(dice_state, range(1,7)))):
        if n_dice >= 3:
            score += v*3
            found_3 = True
        elif n_dice >= 2:
            score += v*2
            found_2 = True
        if found_2 and found_3:
            return score
    return 0.0

def small_straight_payoff(dice_state):
    if dice_state == (1,1,1,1,1,0): # TODO fixme!
        return 15.0
    else:
        return 0.0

def large_straight_payoff(dice_state):
    if dice_state == (0,1,1,1,1,1):
        return 20.0
    else:
        return 0.0

def yahtzee_payoff(dice_state):
    if 5 in dice_state:
        return 50.0
    else:
        return 0.0

def chance_payoff(dice_state):
    return sum((i+1)*count for i, count in enumerate(dice_state))


PAYOFF_LS = [("ones", ones_payoff),
             ("twos", twos_payoff),
             ("threes", threes_payoff),
             ("fours", fours_payoff),
             ("fives", fives_payoff),
             ("sixes", sixes_payoff),
             ("one pair", one_pair_payoff),
             ("two pairs", two_pairs_payoff),
             ("three of a kind", three_of_a_kind_payoff),
             ("four of a kind", four_of_a_kind_payoff),
             ("full house", full_house_payoff),
             ("small straight", small_straight_payoff),
             ("large straight", large_straight_payoff),
             ("Yahtzee", yahtzee_payoff),
             ("chance", chance_payoff)
            ]


