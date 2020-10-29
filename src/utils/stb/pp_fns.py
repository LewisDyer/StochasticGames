# Shut the Box-specific functions

def test(x=0):
    if(x):
        return("this is from the stb folder\nyou set my argument as true!")
    else:
        return("this is from the stb folder")

def lookup(fname):
    functions = {"cover": test}
    return functions[fname]