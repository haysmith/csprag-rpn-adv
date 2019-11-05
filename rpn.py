#!/usr/bin/env python3

import operator


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def print_help():
    print("Accepted Format: arg1 arg2 operator")
    print("Supported Operators:")
    op_string = ""
    for item in operators.keys():
        op_string += item + " "
    print(op_string)

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
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    result = 0
    while True:
        try:
            result = calculate(raw_input("rpn calc> "), result)
        except ValueError:
            continue
        print("Result: ", result)

if __name__ == '__main__':
    main()
