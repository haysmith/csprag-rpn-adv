#!/usr/bin/env python3

import operator
import readline
from colored import fg, bg, attr


color = [fg('114'), fg('220'), fg('205'), fg('99')]

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def print_help():
    print("Accepted Format: " + color[0] + "arg1 " + color[1] + "arg2 " + color[2] + "operator" + attr('reset'))
    op_string = color[2]
    for item in operators.keys():
        op_string += item + " "
    print("Supported Operators: " + op_string + attr('reset'))

def calculate(myarg, prev_result):
    stack = list()
    if myarg == "help":
        print_help()
        raise ValueError
    for token in myarg.split():
        try:
            if token == "r":
                token = prev_result
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        #print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    color_str = ""
    for i, token in enumerate(myarg.split()):
        color_str += color[i] + token + " "
    color_str += attr('reset')
    print(color_str)
    return stack.pop()

def main():
    result = 0
    while True:
        try:
            result = calculate(input("rpn calc> "), result)
        except ValueError:
            continue
        print("Result: ", color[3] + str(result) + attr('reset'))

if __name__ == '__main__':
    main()
