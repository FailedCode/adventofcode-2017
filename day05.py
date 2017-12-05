#!/usr/bin/python

tests = [
    {'in': '0 3 0 1 -3', 'out': 5},
]

with open('input/day05.txt', 'r') as file:
    file_text = file.read()
inputs = map(lambda v: int(v), file_text.split("\n"))


print ""
print "part 1: count steps"


def count_jumps(instructions):
    """
    """
    jumps = 0
    pos = 0
    minpos = 0
    maxpos = len(instructions) - 1
    while True:
        newpos = instructions[pos] + pos
        instructions[pos] += 1
        jumps += 1
        if newpos < minpos or newpos > maxpos:
            return jumps
        pos = newpos


for test in tests:
    if isinstance(test, dict):
        in_value = test.get('in')
        out_value = test.get('out')
        out_result = count_jumps(map(lambda v: int(v), in_value.split()))
        if out_value == out_result:
            print "{} => {} - OK".format(in_value, out_result)
        else:
            print "{} => {} - FAIL ({})".format(in_value, out_result, out_value)

print "puzzle: {}".format(count_jumps(inputs))
