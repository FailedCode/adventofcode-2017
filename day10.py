#!/usr/bin/python

tests = [
    {'in': [3, 4, 1, 5], 'out': 12, 'f': 'tie_a_knot'},
]

with open('input/day10.txt', 'r') as file:
    file_text = file.read()
input_text = file_text.strip()
inputs = map(lambda v: int(v), file_text.split(","))


print ""
print "part 1: group score"


def replace_in_list(source, from_index, replace):
    len_source = len(source)
    len_replace = len(replace) - 1
    i = from_index
    ri = 0
    while ri <= len_replace:
        source[i] = replace[ri]
        i = (i + 1) % len_source
        ri += 1


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


print ""
print "part 2: dense hash"


tests = [
    {'in': '', 'out': 'a2582a3a0e66e6e86e3812dcb672a272', 'f': 'dense_hash'},
    {'in': 'AoC 2017', 'out': '33efeb34ea91902bb2f59c9920caa6cd', 'f': 'dense_hash'},
    {'in': '1,2,3', 'out': '3efbe78a8d82f29979031a4aa0b16a9d', 'f': 'dense_hash'},
    {'in': '1,2,4', 'out': '63960835bcdc130f0b66d7ff4f6a5a8e', 'f': 'dense_hash'},
]


def ascii_list(text):
    if type(text) is not str:
        raise TypeError()
    ascii = list()
    for char in text:
        ascii.append(ord(char))
    return ascii


def sparse_hash(instructions):
    list_length = 256
    round_length = 64
    knot = list()
    for x in xrange(0, list_length):
        knot.append(x)

    p1 = 0
    skip_size = 0
    for round in xrange(0, round_length):
        for i in instructions:
            p2 = (p1 + i) % list_length
            sublist = get_sub_list(knot, p1, p2)
            sublist.reverse()
            replace_in_list(knot, p1, sublist)
            p1 = (p1 + i + skip_size) % list_length
            skip_size += 1
    return knot


def dense_hash(source):
    if type(source) is str:
        source = ascii_list(source)
    source += [17, 31, 73, 47, 23]
    sparse = sparse_hash(source)
    hash = ''
    for block in xrange(0, 256, 16):
        part = sparse[block] ^ sparse[block + 1] ^ sparse[block + 2] ^ sparse[block + 3] ^ sparse[block + 4] ^ sparse[block + 5] ^ sparse[block + 6] ^ sparse[block + 7] ^ sparse[block + 8] ^ sparse[block + 9] ^ sparse[block + 10] ^ sparse[block + 11] ^ sparse[block + 12] ^ sparse[block + 13] ^ sparse[block + 14] ^ sparse[block + 15]
        hash += format(part, 'x').rjust(2, '0')
    return hash


for test in tests:
    in_value = test.get('in')
    out_value = test.get('out')
    func = eval(test.get('f'))
    out_result = func(in_value)
    if out_value == out_result:
        print "'{}' => {} - OK".format(in_value, out_result)
    else:
        print "'{}' => FAIL ".format(in_value)
        print out_result
        print out_value

print "puzzle: {}".format(dense_hash(input_text))
