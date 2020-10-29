# Common functions for preprocessing

def test():
    return("this is from the utils folder")

def lookup(fname):
    functions = {"cover": test}
    return functions[fname]