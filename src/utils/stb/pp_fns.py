# Shut the Box-specific functions
from math import floor, factorial

def test(x=0):
    if(x):
        return("this is from the stb folder\nyou set my argument as true!")
    else:
        return("this is from the stb folder")

def score(n):
    # outputs a prism formula for the score as the sum of covered boards
    # could extend later to count number of boards/use other scoring schemes?
    score_terms = " + ".join([f"b{i}*{i}"for i in range(1, n+1)])
    return(f"formula score = {score_terms};")

def die(d):
   
   return(f"die: [0..{d}] init 0;\n")

def dietoss(d, ndie):
    # defines PRISM code for rolling a given number of d-sided dice

    all_outcomes = d**ndie
    
    probs = [f"{prob_sum(d, ndie, i)}/{all_outcomes}:(die'={i}) & (state'=1)" for i in range(ndie, d*ndie+1)]

    probs = "\n\t\t\t\t\t+ ".join(probs)
    return(f"[die_toss] state=0 -> {probs};")

def nCr(n, r):
    print(n)
    print(r)
    return factorial(n) // factorial(r) // factorial(n-r)

def prob_sum(sides, throws, target):
    # given n d-sided die, gives the number of outcomes that result in the die summing to k

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

def lookup(fname):
    functions = {"score": score, "die": die, "dietoss": dietoss}
    return functions[fname]