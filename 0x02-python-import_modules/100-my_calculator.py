#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args_no = len(sys.argv) - 1
    if args_no != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    math_op = sys.argv[2]
    if math_op != '+' and math_op != '-' and math_op != '*' and math_op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if math_op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif math_op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif math_op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
