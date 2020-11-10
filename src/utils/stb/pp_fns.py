# Shut the Box-specific functions

from math import factorial, floor



def test(x=0):
    if(x):
        return("this is from the stb folder\nyou set my argument as true!")
    else:
        return("this is from the stb folder")

def score(n, newline):
    # outputs a prism formula for the score as the sum of covered boards
    # could extend later to count number of boards/use other scoring schemes?
    score_terms = " + ".join([f"b{i}*{i}"for i in range(1, n+1)])
    return(f"formula score = {score_terms};")

def die(d, newline):
    return(f"die: [0..{d}] init 0;\n")

def dietoss(d, ndie, newline):
    # defines PRISM code for rolling a given number of d-sided dice

    all_outcomes = d**ndie
    
    probs = [f"{prob_sum(d, ndie, i)}/{all_outcomes}:(die'={i}) & (state'=1)" for i in range(ndie, d*ndie+1)]

    probs = f"{newline}\t\t\t\t\t+ ".join(probs)
    return(f"[die_toss] state=0 -> {probs};")

def prob_sum(sides, throws, target):
    # given n throws of a d-sided die, gives the number of outcomes that result in the die throws summing to k
    # could improve this with dynamic programming, but not a priority

    # no more throws left
    if throws == 0:
        return 1 if (target == 0) else 0 # check if sum has been reached

    # sum unreachable
    if (target < 0) or (throws * sides < target) or (throws > target):
        return 0

    outcomes = 0

    for i in range(1, sides+1):
        # all possibilities for dice value
        outcomes += prob_sum(sides, throws-1, target-i)

    return outcomes

def high_board(covers):
    # given a list of boards, prioritise the boards with the largest numbers
    covers.sort(reverse=True)

    return(covers)

def low_board(covers):
    # prioritise boards with lowest/most numbers. If there's a tie, choose the covering with the lower numbers.
    covers.sort()
    covers.sort(key=len, reverse=True)
    return(covers)

def list_covers(b, strategy, newline):

    strategy_lookup = {1: high_board, 2: low_board}
    # given b boards to cover and a strategy to prioritise boards, returns PRISM model code presenting all possible board coverings

    # step 1: generate partitions
    # step 2: order partitions
    # step 3: convert to PRISM code

    all_covers = []
    for i in range(1, b+1):
        parts = [p for p in partitions(i) if len(set(p)) == len(p)] # get partitions with distinct parts
        if strategy:
            covers = strategy_lookup[strategy](parts)
        else:
            covers = parts.sort(reverse=True) # tidy up arrangement even with no strategy

        if covers:
            all_covers.append(covers_to_prism(i, covers, strategy!=0, newline))
    
    return f"\n{newline}".join(all_covers)

def covers_to_prism(n, covers, determ, newline):
    # given a list of covers for a value n, convert to PRISM model code
    negate_states = ""
    all_covers = []
    for i in range(len(covers)):
        cover = covers[i]
        action_label = f"[cover{''.join(str(c) for c in cover)}]"

        if determ & i > 0:
            prev_states = [convert_cover(c) for c in covers[:i]]
            negate_states = f" !({' | '.join(prev_states)}) &"

        prism_cover = f"{action_label} state=1 & die={n} &{negate_states} {convert_cover(cover)} -> (state'=0);"
        all_covers.append(prism_cover)


    prev_states = [convert_cover(c) for c in covers]
    negate_states = f" !({' | '.join(prev_states)})"

    all_covers.append(f"[ncover] state=1 & die={n} & {negate_states} -> (state'=2);") 
    return(newline.join(all_covers))

def convert_cover(cover):
    # given a single cover, convert it to a PRISM expression
    bools = [f"b{i}=0" for i in cover]

    return(f"({' & '.join(bools)})")

def partitions(n):
    # all partitions, allowing repetition (e.g multiple ones)
    all_parts = set()
    all_parts.add((n, ))
    for i in range(1, n):
        for j in partitions(n - i):
            all_parts.add(tuple(sorted((i, ) + j, reverse=True)))
    
    return all_parts

def list_boards(b, newline):
    # given b boards, produces PRISM mode producing these board modules
    return((newline*2).join([produce_board(i, b, newline) for i in range(1,b+1)]))

def produce_board(current, b, newline):
    # produce PRISM code for one board
    parts = []
    for i in range(1, b+1):
        parts.extend([p[::-1] for p in partitions(i) if len(set(p)) == len(p) and current in p])

    parts.sort(key=len, reverse=False)

    board_module = [f"module board{current}", "", f"\tb{current} : [0..1];", ""]

    for p in parts:
        board_module.append(f"\t[cover{''.join([str(i) for i in p])}] b{current}=0 -> (b{current}'=1);")
    
    board_module.append("")
    board_module.append("endmodule")
    
    return(newline.join(board_module))

def lookup(fname):
    functions = {"score": score, "die": die, "dietoss": dietoss, "listcovers": list_covers, "listboards": list_boards}
    return functions[fname]
