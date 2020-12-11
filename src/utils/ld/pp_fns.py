from itertools import product

def list_p1_dice(n_die, newLine):
    dice_list = []
    for i in range(1, n_die+1):
        dice_list.append(f"p1_d{i}")
    
    return ", ".join(dice_list) + ","

def formulas(p1_die, p2_die, newLine):
    # PRISM code for the formulas (p1_(i)s, p2_(i)s, all_(i)s)
    output = []
    for i in range(6):
        output.append(create_formula(p1_die, i+1, 1))
    output.append("")
    for i in range(6):
        output.append(create_formula(p2_die, i+1, 2))
    output.append("")
    for i in range(6):
        output.append(f"formula all_{i+1}s = p1_{i+1}s + p2_{i+1}s;")

    return newLine.join(output)

def create_formula(p1_die, value, p):
    # PRISM code for a single formula, p{p}_{value}s
    output = []
    output.append(f"formula p{p}_{value}s = (p{p}_d1 = {value} ? 1 : 0)")
    for die in range(2, p1_die+1):
        output.append(f"(p{p}_d{die} = {value} ? 1 : 0)")
    return " + ".join(output) + ";"

def init_dice(no_die, p, newLine):
    # PRISM code for variable declarations for each die
    output = []
    for i in range(1, no_die+1):
        output.append(f"p{p}_d{i} : [0..6] init 0;")
    return newLine.join(output)

def roll_dice(no_die, p, newLine):
    # PRISM code to roll all dice from a player
    output = []

    for i in range(1, no_die+1):
        output.append(roll_die(i, p, newLine))

    return newLine.join(output)

def roll_die(die_no, p, newLine):
    # PRISM code to roll a single die
    if die_no == 1:
        prelude = f"[roll_die{die_no}] phase=0 & p{p}_{die_no} = 0 -"
    else:
        prelude = f"[roll_die{die_no}] phase=0 & p{p}_{die_no} != 0 & p{p}_{die_no-1} != 0 -"

    output = []
    output.append(f"{prelude}> 1/6: (p{p}_d1'=1)")
    for i in range(2, 7):
        output.append(f"{' '*len(prelude)}+ 1/6: (p{p}_d{i}'={i})")
    
    return newLine.join(output) + ";"
      
def define_init_bid(strat, p1_die, p2_die, p, newLine):
    strat_lookup = {0: bid_random, 1: bid_random_in_hand}

    return strat_lookup[strat](p, p1_die, p2_die, newLine)

def bid_random(p, p1_die, p2_die, newLine):
    # choose a totally random bid face and quantity, even if it's not in hand
    prelude = f"[p{p}_bid_init] phase=1 -"
    no_options = 6 * (p1_die+p2_die)
    output = []
    output.append(f"{prelude}> 1/{no_options}: (p{p}_bid_face' = 1) & (p{p}_bid_quat' = 1)")
    for face in range(1,7):
        for quat in range(1, (p1_die+p2_die+1)):
            if (face, quat) != (1, 1): # exclude current case
                output.append(f"{' '*len(prelude)}+ 1/{no_options}: (p{p}_bid_face' = {face}) & (p{p}_bid_quat' = {quat})")
            
    return newLine.join(output) + ';'

    return newLine.join(output) + ";"
def bid_random_in_hand(p, p1_die, p2_die, newLine):
    # choose a random dice in your hand and set its face as your bid, with quantity 1.
    prelude = f"[p{p}_bid_init] phase=1 -"
    no_die = p1_die if p == 1 else p2_die
    output = []
    output.append(f"{prelude}> 1/{no_die}: (p{p}_bid_face' = p{p}_d1) & (p{p}_bid_quat' = 1)")
    for i in range(2, no_die+1):
        output.append(f"{' '*len(prelude)}+ 1/{no_die}: (p{p}_bid_face' = p{p}_d{i}) & (p{p}_bid_quat' = 1)")

    return newLine.join(output) + ';'

def lookup(fname):
    functions = {"list_p1_dice": list_p1_dice, "formulas": formulas, "init_dice": init_dice,
                 "roll_dice": roll_dice, "define_init_bid": define_init_bid}
    return functions[fname]
