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
    in_value = test.get('in')
    out_value = test.get('out')
    out_result = count_jumps(map(lambda v: int(v), in_value.split()))
    if out_value == out_result:
        print "{} => {} - OK".format(in_value, out_result)
    else:
        print "{} => {} - FAIL ({})".format(in_value, out_result, out_value)

print "puzzle: {}".format(count_jumps(list(inputs)))

print ""
print "part 2:"


def count_jumps_extended(instructions):
    jumps = 0
    pos = 0
    minpos = 0
    maxpos = len(instructions) - 1
    while True:
        newpos = instructions[pos] + pos
        if instructions[pos] > 2:
            instructions[pos] -= 1
        else:
            instructions[pos] += 1
        jumps += 1
        if newpos < minpos or newpos > maxpos:
            # print ' '.join(map(lambda v: str(v), instructions))
            return jumps
        pos = newpos


tests = [
    {'in': '0 3 0 1 -3', 'out': 10},
]

for test in tests:
    in_value = test.get('in')
    out_value = test.get('out')
    out_result = count_jumps_extended(map(lambda v: int(v), in_value.split()))
    if out_value == out_result:
        print "{} => {} - OK".format(in_value, out_result)
    else:
        print "{} => {} - FAIL ({})".format(in_value, out_result, out_value)

print "puzzle: {}".format(count_jumps_extended(list(inputs)))
