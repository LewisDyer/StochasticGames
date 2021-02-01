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

def lookup(fname):
    functions = {"end_formulas": end_formulas, "pair_formulas": pair_formulas, "bust_formulas": bust_formulas, "move_formulas": move_formulas, "endpos_formulas": endpos_formulas}
    return functions[fname]