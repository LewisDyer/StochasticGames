import argparse
import pathlib
import importlib
import re

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

parser = argparse.ArgumentParser()
parser.add_argument('input', type=pathlib.Path)
parser.add_argument('output', type=pathlib.Path)

args = parser.parse_args()

with args.input.open('r') as f_in, args.output.open('w') as f_out:
    for line in f_in:
        template = re.search(r'@(.*?)@', line)
        if template:
            location, fname, params = parse_template(template.group(1))
            fn = get_function(location, fname)
            params = [int(p) for p in params]
            f_out.write(fn(*params) + '\n')
        else:
            f_out.write(line + '\n')


