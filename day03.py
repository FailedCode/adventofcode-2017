#!/usr/bin/python

tests = [
    {'in': 1, 'out': 0},
    {'in': 12, 'out': 3},
    {'in': 23, 'out': 2},
    {'in': 1024, 'out': 31},
    347991
]

print ""
print "part 1: manhattan distance"


"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23  -> ...
"""


def spiral_manhattan_distance(target_value):
    if target_value < 2:
        return 0
    value = 1
    x = 0
    y = 0
    ring_nr = 0
    number_per_ring = 8
    number_this_ring = 0
    directions = {'r': [1, 0], 'u': [0, 1], 'l': [-1, 0], 'd': [0, -1]}
    direction = 'r'
    movements = []
    while value != target_value:
        movements.append(direction)
        d = directions.get(direction)
        x += d[0]
        y += d[1]
        value += 1
        number_this_ring += 1
        if number_this_ring > ring_nr * number_per_ring:
            number_this_ring = 1
            ring_nr += 1
            # print "ring {}, begins with {}".format(ring_nr, value)
        if number_this_ring >= ring_nr * number_per_ring * 0.75:
            direction = 'r'
        elif number_this_ring >= ring_nr * number_per_ring * 0.50:
            direction = 'd'
        elif number_this_ring >= ring_nr * number_per_ring * 0.25:
            direction = 'l'
        else:
            direction = 'u'
    # print movements
    # print "[{}, {}]".format(x, y)
    return abs(x) + abs(y)


for test in tests:
    if isinstance(test, dict):
        in_value = test.get('in')
        out_value = test.get('out')
        out_result = spiral_manhattan_distance(in_value)
        if out_value == out_result:
            print "{} => {} - OK".format(in_value, out_result)
        else:
            print "{} => {} - FAIL ({})".format(in_value, out_result, out_value)
    else:
        print "{} => {}".format(test, spiral_manhattan_distance(test))


print ""
print "part 2: spiral sum"


tests = [
    {'in': 1, 'out': 2},
    {'in': 12, 'out': 23},
    {'in': 23, 'out': 25},
    347991
]


def spiral_sum(target_value):

    def sum_adjacent(_dict, x, y):
        v = []
        v.append(_dict.get("{},{}".format(x + 1, y), 0))
        v.append(_dict.get("{},{}".format(x - 1, y), 0))
        v.append(_dict.get("{},{}".format(x, y + 1), 0))
        v.append(_dict.get("{},{}".format(x, y - 1), 0))
        v.append(_dict.get("{},{}".format(x + 1, y + 1), 0))
        v.append(_dict.get("{},{}".format(x - 1, y - 1), 0))
        v.append(_dict.get("{},{}".format(x + 1, y - 1), 0))
        v.append(_dict.get("{},{}".format(x - 1, y + 1), 0))
        return reduce(lambda x, y: x + y, v)

    value = 1
    x = 0
    y = 0
    ring_nr = 0
    number_per_ring = 8
    number_this_ring = 0
    fieldValues = {}
    fieldValues["0,0"] = 1
    directions = {'r': [1, 0], 'u': [0, 1], 'l': [-1, 0], 'd': [0, -1]}
    direction = 'r'
    while value <= target_value:
        d = directions.get(direction)
        x += d[0]
        y += d[1]
        value += 1

        thisfield = sum_adjacent(fieldValues, x, y)

        if thisfield > target_value:
            return thisfield

        fieldValues["{},{}".format(x, y)] = thisfield

        number_this_ring += 1
        if number_this_ring > ring_nr * number_per_ring:
            number_this_ring = 1
            ring_nr += 1
        if number_this_ring >= ring_nr * number_per_ring * 0.75:
            direction = 'r'
        elif number_this_ring >= ring_nr * number_per_ring * 0.50:
            direction = 'd'
        elif number_this_ring >= ring_nr * number_per_ring * 0.25:
            direction = 'l'
        else:
            direction = 'u'
    return value


for test in tests:
    if isinstance(test, dict):
        in_value = test.get('in')
        out_value = test.get('out')
        out_result = spiral_sum(in_value)
        if out_value == out_result:
            print "{} => {} - OK".format(in_value, out_result)
        else:
            print "{} => {} - FAIL ({})".format(in_value, out_result, out_value)
    else:
        print "{} => {}".format(test, spiral_sum(test))
