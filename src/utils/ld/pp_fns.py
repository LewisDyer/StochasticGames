# Liar's Dice-specific functions

def int_sols(n):
    # given a natural number n, returns the set of non-negative integer solutions where x_1 + x_2 + ... + x_6 = n.
    # I know this is O(n^6)

    solutions = []
    for x_1 in range(n+1):
        for x_2 in range(n+1):
            for x_3 in range(n+1):
                for x_4 in range(n+1):
                    for x_5 in range(n+1):
                        for x_6 in range(n+1):
                            # oh no
                            if x_1 + x_2 + x_3 + x_4 + x_5 + x_6 == n:
                                solutions.append([x_1, x_2, x_3, x_4, x_5, x_6])
    return(len(solutions), solutions)

def roll_dice(n_die, p, newLine):
    # given a number of six-sided dice, and a player number, produces PRISM code for rolling those dice 


def partitions(n):
    # all partitions, allowing repetition (e.g multiple ones)
    all_parts = list()
    all_parts.append((n, ))
    for i in range(1, n):
        for j in partitions(n - i):
            all_parts.append(tuple(sorted((i, ) + j, reverse=True)))
    
    return all_parts   


def lookup(fname):
    functions = {"int_sols": int_sols}
    return functions[fname]
