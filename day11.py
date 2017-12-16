#!/usr/bin/python


with open('input/day11.txt', 'r') as file:
    file_text = file.read()
inputs = file_text


print ""
print "part 1: max steps"


tests = [
    {'in': 'ne,ne,ne', 'out': 3, 'f': 'hex_min_steps'},
    {'in': 'ne,ne,sw,sw', 'out': 0, 'f': 'hex_min_steps'},
    {'in': 'ne,ne,s,s', 'out': 2, 'f': 'hex_min_steps'},
    {'in': 'se,sw,se,sw,sw', 'out': 3, 'f': 'hex_min_steps'},
]

"""
  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
"""

directions = {
    'se': [-1, 1],
    's': [-1, 0],
    'sw': [0, -1],
    'nw': [1, -1],
    'n': [1, 0],
    'ne': [0, 1],
}


def description_to_coords(text):
    coords = list()
    for d in text.split(','):
        coords.append(directions.get(d))
    return coords


def hex_min_steps(source):
    coords = description_to_coords(source)
    x = 0
    y = 0
    for c in coords:
        x += c[0]
        y += c[1]
    return (abs(x) + abs(y) + abs(x + y)) / 2


for test in tests:
    in_value = test.get('in')
    out_value = test.get('out')
    func = eval(test.get('f'))
    out_result = func(in_value)
    if out_value == out_result:
        print "{} => {} - OK".format(in_value, out_result)
    else:
        print "{} => {} - FAIL ({})".format(in_value, out_result, out_value)

print "puzzle: {}".format(hex_min_steps(inputs))


print ""
print "part 2: max steps"


def hex_max_steps(source):
    coords = description_to_coords(source)
    x = 0
    y = 0
    steps = 0
    for c in coords:
        x += c[0]
        y += c[1]
        d = (abs(x) + abs(y) + abs(x + y)) / 2
        if d > steps:
            steps = d
    return steps


print "puzzle: {}".format(hex_max_steps(inputs))
