from itertools import product

def get_rolls(n_die, p, newLine):
    # get prism model code to roll n dice
    all_rolls = list(product(range(1,7), repeat=n_die))
    no_rolls = 6 ** n_die

    output = []
    prelude_string = "[roll_dice] phase=0 -" # keeps the expression aligned later on
    output.append(f"{prelude_string}> 1/{no_rolls}: {roll_to_prism(all_rolls[0], p)}")
    for roll in all_rolls[1:]:
        output.append(f"{' ' * len(prelude_string)}+ 1/{no_rolls}: {roll_to_prism(roll, p)}")

    return(newLine.join(output)) + ";"


def roll_to_prism(roll, p):
    # given a tuple of n dice values, returns prism code to assign each die to its appropriate value
    output = []
    for i, die in enumerate(roll):
        output.append(f"(p{p}_d{i+1}'={die})")
    
    return " & ".join(output)


def lookup(fname):
    functions = {"get_rolls": get_rolls}
    return functions[fname]