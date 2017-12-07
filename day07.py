#!/usr/bin/python

tests = [
    {'in': """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""", 'out': 'tknk'},
]

with open('input/day07.txt', 'r') as file:
    file_text = file.read()
inputs = file_text


print ""
print "part 1: find the bottom programm"


def find_bottom_programm(text):
    programm_weight = {}
    programm_sub = {}
    # parse
    for line in text.split("\n"):
        p1 = line.find('(')
        p2 = line.find(')')
        p3 = line.find('->')
        name = line[:p1].strip()
        weight = int(line[p1 + 1:p2])
        programm_weight[name] = weight
        if p3 != -1:
            subprogramms = line[p3 + 3:].split(", ")
            programm_sub[name] = subprogramms
    # count parents
    parents = {}
    for k in programm_sub:
        if k not in parents:
            parents[k] = 0
        sub = programm_sub[k]
        for s in sub:
            if s not in parents:
                parents[s] = 1
            parents[s] += 1
    return min(parents, key=parents.get)


for test in tests:
    in_value = test.get('in')
    out_value = test.get('out')
    out_result = find_bottom_programm(in_value)
    if out_value == out_result:
        print "{} => {} - OK".format(in_value, out_result)
    else:
        print "{} => {} - FAIL ({})".format(in_value, out_result, out_value)

print "puzzle: {}".format(find_bottom_programm(inputs))
