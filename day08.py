#!/usr/bin/python

tests = [
    {'in': """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""", 'out': 1, 'f': 'calculate_register_value'},
]

with open('input/day08.txt', 'r') as file:
    file_text = file.read()
inputs = file_text


print ""
print "part 1: largest value in any register"


def calculate_register_value(instructionText):
    lines = instructionText.split("\n")
    register = {}
    for line in lines:
        reg, instruction, value, _if, reg_test, symbol, value_test = line.split(" ")
        condition = "{} {} {}".format(register.get(reg_test, 0), symbol, value_test)
        if eval(condition):
            reg_value = register.get(reg, 0)
            if instruction == 'inc':
                reg_value += int(value)
            if instruction == 'dec':
                reg_value -= int(value)
            register[reg] = reg_value
    maxKey = max(register, key=register.get)
    return register[maxKey]


for test in tests:
    in_value = test.get('in')
    out_value = test.get('out')
    func = eval(test.get('f'))
    out_result = func(in_value)
    if out_value == out_result:
        print "{} => {} - OK".format(in_value, out_result)
    else:
        print "{} => {} - FAIL ({})".format(in_value, out_result, out_value)

print "puzzle: {}".format(calculate_register_value(inputs))
