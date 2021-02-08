from itertools import permutations
from collections import defaultdict
from math import factorial
from functools import reduce

def end_formulas(players, newLine):
    output = []
    for p in range(1, players+1):
        output.append(f"formula p{p}_end = p{p}_move > p{p}_pos;")
    output.append(f"formula game_over = {' | '.join([f'p{p}_end' for p in range(1, players+1)])};")

    return newLine.join(output)

def pair_formulas(players, no_sides, newLine):
    output = []
    for p in range(1, players+1):
        output.append(f"formula p{p}_pairs = {' + '.join([f'((p{p}_{i}s >= 2) ? 1 : 0)' for i in range(1, no_sides+1)])}")
    
    return newLine.join(output)

def bust_formulas(players, no_sides, newLine):
    output = []
    for p in range(1, players+1):
        bust_formula = [f'(p{p}_pairs >= 2)']
        for i in range(1, no_sides+1):
            bust_formula.append(f"(p{p}_{i}s >= 3)")
        output.append(f"formula p{p}_bust = {' | '.join(bust_formula)};")
    
    return newLine.join(output)

def move_formulas(players, no_sides, newLine):
    output = []
    for p in range(1, players+1):
        move_amount = f"({' + '.join([f'{i} * p{p}_{i}s' for i in range(1, no_sides+1)])})"
        output.append(f"formula p{p}_move = p{p}_bust ? 0 : {move_amount};")
    
    return newLine.join(output)

def endpos_formulas(players, newLine):
    output = []
    for p in range(1, players+1):
        output.append(f"formula p{p}_end_pos = p{p}_pos + (p{p}_end ? no_spaces : 0);")
    
    return newLine.join(output)

def def_player(p, no_sides, no_dice, strategy, newLine):
    output = []
    # initially add all indented content - get other content later

    output.append(f"p{p}_chosen_dice : [1..no_dice] init 1;")
    
    output.append("")

    output.append(f"{newLine}".join(die_counts(p, no_sides, newLine)))

    output.append("")

    output.append(pick_die(p, no_dice, strategy, newLine))

    output.append("")

    output.append(die_rolling(p, no_dice, no_sides, newLine))

    inner_output=f"{newLine}".join(output)

    




    final_output = [f"module player{p}", "", inner_output, "", "endmodule"]

    return newLine.join(final_output)

def die_rolling(p, no_dice, no_sides, newLine):

    output = []

    for no_chose in range(1, no_dice+1):

        output.append(one_step_rolls(p, no_chose, no_sides, newLine))
    
        output.append("")
    
    print(output)
    
    return newLine.join(output)




def partitions(n):
    # all partitions, allowing repetition (e.g multiple ones)
    all_parts = set()
    all_parts.add((n, ))
    for i in range(1, n):
        for j in partitions(n - i):
            all_parts.add(tuple(sorted((i, ) + j, reverse=True)))
    
    return all_parts

def roll_n_dice(no_dice, no_sides):

    parts = partitions(no_dice)

    valid_parts = [part for part in parts if len(part) <= no_sides]

    valid_parts = [list(part) + [0]*(no_sides-len(part)) for part in valid_parts] # zero-pad each part

    perms = []

    for part in valid_parts:
        perms.extend(list(set(permutations(part))))

    perms.sort(reverse=True)
    
    print(perms)
    return perms

def one_step_rolls(p, no_rolled, no_sides, newLine):
    output = []
    no_options = no_sides ** no_rolled

    perms = roll_n_dice(no_rolled, no_sides)

    output.append(f"[p{p}_roll_{no_rolled}_dice] state=1 & p{p}_chosen_dice={no_rolled} ->")

    perms_output = []
    prob_sum = 0
    for perm in perms:
        prob_perm = int(factorial(no_rolled) / reduce(lambda x, y: x * y, [factorial(x) for x in perm], 1))
        
        set_count = " & ".join([f"(p{p}_{i}s'={perm[i-1]})" for i in range(1, no_sides+1)])
        perms_output.append(f"{prob_perm}/{no_options} : {set_count}")
    
    output.append(f" + {newLine}".join(perms_output) + ";")

    return newLine.join(output)







#pe = roll_n_dice(3, 6)
#one_step_rolls(1, pe, 3, 6, "")

def pick_die(p, no_dice, strategy, newLine):
    strategy_lookup = {1: random}

    output = [f"[p{p}_pick_dice] state=0 ->"]
    output.append(strategy_lookup[strategy](p, no_dice, newLine))
    return f"{newLine}\t".join(output)



def random(p, no_dice, newLine):
    # choose a random number of dice to roll from 1 to no_dice
    print("start random")
    choices = []

    for i in range(1, no_dice+1):
        choices.append(f"1/{no_dice} : (p{p}_chosen_dice' = {i})")
    return f" + {newLine}\t".join(choices) + ";"
    
    
def die_counts(p, no_sides, newLine):
    output = []
    for i in range(1, no_sides+1):
        output.append(f"p{p}_{i}s : [0..no_dice] init 0;")
    return output



def lookup(fname):
    functions = {"end_formulas": end_formulas, "pair_formulas": pair_formulas, "bust_formulas": bust_formulas, "move_formulas": move_formulas, "endpos_formulas": endpos_formulas, "def_player": def_player}
    return functions[fname]