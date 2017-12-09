#!/usr/bin/python

import re

tests = [
    {'in': '<<<<>', 'out': '', 'f': 'clean_garbage'},
    {'in': '<{!>}>', 'out': '', 'f': 'clean_garbage'},
    {'in': '<!!>', 'out': '', 'f': 'clean_garbage'},
    {'in': '<!!!>>', 'out': '', 'f': 'clean_garbage'},
    {'in': '<{o"i!a,<{i<a>', 'out': '', 'f': 'clean_garbage'},
    {'in': "{}", 'out': 1, 'f': 'group_score'},
    {'in': "{{{}}}", 'out': 6, 'f': 'group_score'},
    {'in': "{{},{}}", 'out': 5, 'f': 'group_score'},
    {'in': "{{{},{},{{}}}}", 'out': 16, 'f': 'group_score'},
    {'in': "{<a>,<a>,<a>,<a>}", 'out': 1, 'f': 'group_score'},
    {'in': "{{<ab>},{<ab>},{<ab>},{<ab>}}", 'out': 9, 'f': 'group_score'},
    {'in': "{{<!!>},{<!!>},{<!!>},{<!!>}}", 'out': 9, 'f': 'group_score'},
    {'in': "{{<a!>},{<a!>},{<a!>},{<ab>}}", 'out': 3, 'f': 'group_score'},
]

with open('input/day09.txt', 'r') as file:
    file_text = file.read()
inputs = file_text


print ""
print "part 1: group score"


def clean_garbage(chars):
    chars = re.sub('!.', '', chars)
    chars = re.sub('<[^>.]*>', '', chars)
    return chars


def group_score(chars):
    chars = clean_garbage(chars)
    score = 0
    depth = 0
    for c in chars:
        if c == '{':
            depth += 1
            score += depth
        if c == '}':
            depth -= 1
    return score


for test in tests:
    in_value = test.get('in')
    out_value = test.get('out')
    func = eval(test.get('f'))
    out_result = func(in_value)
    if out_value == out_result:
        print "{} => {} - OK".format(in_value, out_result)
    else:
        print "{} => {} - FAIL ({})".format(in_value, out_result, out_value)

print "puzzle: {}".format(group_score(inputs))
