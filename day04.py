#!/usr/bin/python

tests = [
    {'in': 'aa bb cc dd ee', 'out': True},
    {'in': 'aa bb cc dd aa', 'out': False},
    {'in': 'aa bb cc dd aaa', 'out': True},
]

with open('input/day04.txt', 'r') as file:
    file_text = file.read()
inputs = file_text.split("\n")

print ""
print "part 1: duplicate words"


def is_passphrase_valid(phrase):
    """
        a set can only contain unique values
        so if the list and the set are the same size, no word was removed
    """
    word_list = phrase.split(" ")
    return len(word_list) == len(set(word_list))


for test in tests:
    if isinstance(test, dict):
        in_value = test.get('in')
        out_value = test.get('out')
        out_result = is_passphrase_valid(in_value)
        if out_value == out_result:
            print "{} => {} - OK".format(in_value, out_result)
        else:
            print "{} => {} - FAIL ({})".format(in_value, out_result, out_value)

valids = 0
for phrase in inputs:
    valids += is_passphrase_valid(phrase)
print "valid inputs: {}".format(valids)

print ""
print "part 2:"


def is_passphrase_valid_extended(phrase):
    """
        each list item is alphabetically sorted,
        and again the value is added to the set uniquely
    """
    word_list = phrase.split(" ")
    word_set = set(map(lambda v: ''.join(sorted(v)), word_list))
    return len(word_list) == len(word_set)


tests = [
    {'in': 'abcde fghij', 'out': True},
    {'in': 'abcde xyz ecdab', 'out': False},
    {'in': 'a ab abc abd abf abj', 'out': True},
    {'in': 'iiii oiii ooii oooi oooo', 'out': True},
    {'in': 'oiii ioii iioi iiio', 'out': False},
]

for test in tests:
    if isinstance(test, dict):
        in_value = test.get('in')
        out_value = test.get('out')
        out_result = is_passphrase_valid_extended(in_value)
        if out_value == out_result:
            print "{} => {} - OK".format(in_value, out_result)
        else:
            print "{} => {} - FAIL ({})".format(in_value, out_result, out_value)

valids = 0
for phrase in inputs:
    valids += is_passphrase_valid_extended(phrase)
print "valid inputs: {}".format(valids)
