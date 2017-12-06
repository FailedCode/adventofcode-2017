#!/usr/bin/python

tests = [
    {'in': '0 2 7 0', 'out': 5},
]

with open('input/day06.txt', 'r') as file:
    file_text = file.read()
inputs = map(lambda v: int(v), file_text.split())


print ""
print "part 1: count steps"


def redistribute_count(banks):

    def highestValueIndex(items):
        highest_index = 0
        highest_value = items[0]
        for index, value in enumerate(items):
            if value > highest_value:
                highest_value = value
                highest_index = index
        return highest_index

    """
        1. find highest bank
            - break tie by lowest id
        2. remove blocks from selected, each following block +1
        3. add configuration for loop check
    """
    bank_length = len(banks)
    count = 0
    configuration = '-'.join(map(lambda v: str(v), banks))
    configurations = set()
    while configuration not in configurations:
        configurations.add(configuration)
        pos = highestValueIndex(banks)
        blocks = banks[pos]
        banks[pos] = 0
        while blocks:
            pos = (pos + 1) % bank_length
            banks[pos] += 1
            blocks -= 1
        count += 1
        configuration = '-'.join(map(lambda v: str(v), banks))
    return count


for test in tests:
    in_value = test.get('in')
    out_value = test.get('out')
    out_result = redistribute_count(map(lambda v: int(v), in_value.split()))
    if out_value == out_result:
        print "{} => {} - OK".format(in_value, out_result)
    else:
        print "{} => {} - FAIL ({})".format(in_value, out_result, out_value)

print "puzzle: {}".format(redistribute_count(list(inputs)))

print ""
print "part 2: count loop"

tests = [
    {'in': '0 2 7 0', 'out': 4},
]


def redistribute_loop_count(banks):

    def highestValueIndex(items):
        highest_index = 0
        highest_value = items[0]
        for index, value in enumerate(items):
            if value > highest_value:
                highest_value = value
                highest_index = index
        return highest_index

    """
        instead of the count, we calculate the
    """
    bank_length = len(banks)
    count = 0
    configuration = '-'.join(map(lambda v: str(v), banks))
    configurations = set()
    configuration_list = list()
    while configuration not in configurations:
        configurations.add(configuration)
        configuration_list.append(configuration)
        pos = highestValueIndex(banks)
        blocks = banks[pos]
        banks[pos] = 0
        while blocks:
            pos = (pos + 1) % bank_length
            banks[pos] += 1
            blocks -= 1
        count += 1
        configuration = '-'.join(map(lambda v: str(v), banks))
    return len(configuration_list) - configuration_list.index(configuration)


for test in tests:
    in_value = test.get('in')
    out_value = test.get('out')
    out_result = redistribute_loop_count(map(lambda v: int(v), in_value.split()))
    if out_value == out_result:
        print "{} => {} - OK".format(in_value, out_result)
    else:
        print "{} => {} - FAIL ({})".format(in_value, out_result, out_value)

print "puzzle: {}".format(redistribute_loop_count(list(inputs)))
