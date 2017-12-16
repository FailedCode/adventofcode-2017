#!/usr/bin/python

tests = [
    {'in': [3, 4, 1, 5], 'out': 12, 'f': 'tie_a_knot'},
]

with open('input/day10.txt', 'r') as file:
    file_text = file.read()
inputs = map(lambda v: int(v), file_text.split(","))


print ""
print "part 1: group score"


def replace_in_list(source, from_index, replace):
    len_source = len(source)
    len_replace = len(replace) - 1
    i = from_index
    ri = 0
    # print "replace: "+str(replace)+ " from "+ str(from_index)
    while ri <= len_replace:
        # print "{}, {}".format(i, ri)
        source[i] = replace[ri]
        i = (i + 1) % len_source
        ri += 1
    # print source


def get_sub_list(source, from_index, to_index):
    copy = list(source)
    if to_index < from_index:
        to_index += len(copy)
        copy = copy + copy
    return copy[from_index:to_index]


def tie_a_knot(list_length, instructions):
    knot = list()
    for x in xrange(0, list_length):
        knot.append(x)
    p1 = 0
    skip_size = 0
    for i in instructions:
        p2 = (p1 + i) % list_length
        sublist = get_sub_list(knot, p1, p2)
        sublist.reverse()
        replace_in_list(knot, p1, sublist)
        p1 = (p1 + i + skip_size) % list_length
        skip_size += 1
    return knot[0] * knot[1]


for test in tests:
    in_value = test.get('in')
    out_value = test.get('out')
    func = eval(test.get('f'))
    out_result = func(5, in_value)
    if out_value == out_result:
        print "{} => {} - OK".format(in_value, out_result)
    else:
        print "{} => {} - FAIL ({})".format(in_value, out_result, out_value)

print "puzzle: {}".format(tie_a_knot(256, inputs))

