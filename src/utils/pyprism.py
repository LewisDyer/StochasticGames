import argparse
import pathlib
import importlib
import re
import csv

def parse_template(template):
    ### parse template into each part
    words = template.split(' ')
    if words == []:
        return("")
    location = None
    function = None
    params = []
    if '/' in words[0]: # location specified
        location, function = words[0].split('/')
    else:
        function = words[0]
    params = words[1:]

    return (location, function, params)

def get_function(location, fname):
    # given a location (potentially null) and a function name, returns the function to call.
    if location:
        functions = importlib.import_module(f'{location}.pp_fns')
    else:
        functions = importlib.import_module('pp_fns')
    
    return functions.lookup(fname)

def check_int(s):
    # given a string, checks if it's an integer (without explicit type conversion)
    if s[0] == '-':
        return s[1:].isdigit()
    return s.isdigit()

def set_params(p_values):
    # allows variables to be given specific values externally, either with a .csv file or via user input
    param_lookup = {}
    if p_values:
        # don't try to open file if no arg given
        with p_values.open('r') as p_csv:
            param_lookup = csv.reader(p_csv)
            for p in param_lookup:
                param_lookup[p[0]] = int(p[1])
   
    return param_lookup

def replace_params(params, param_lookup):
    # given a list of arguments for a function, gives them specific values (either from a lookup dictionary or from user input if needed)
    for i, param in enumerate(params):
        if not check_int(param):
            print(param)
            print(param_lookup)
            # only applicable for variable parameters, not constants
            if param not in param_lookup:
            # accept user input if param not found in csv file
                p = " "
                while not check_int(p):
                    p = input(f"Enter value for {param}:")

                param_lookup[param] = p
            else:
                params[i] = param_lookup[param]

    return params
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=pathlib.Path)
    parser.add_argument('output', type=pathlib.Path)
    parser.add_argument('params', type=pathlib.Path, nargs='?', default=None)

    args = parser.parse_args()

    param_lookup = set_params(args.params)

    with args.input.open('r') as f_in, args.output.open('w') as f_out:
        for line in f_in:
            template = re.search(r'@(.*?)@', line)
            if template:
                location, fname, params = parse_template(template.group(1))
                
                if params:
                    params = replace_params(params, param_lookup)
                fn = get_function(location, fname)
                
                f_out.write(fn(*params) + '\n')
            else:
                f_out.write(line)


