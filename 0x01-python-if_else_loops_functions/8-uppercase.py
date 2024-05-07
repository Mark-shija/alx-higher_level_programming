#!/usr/bin/python3
def uppercase(str):
    for input_str in str:
        if ord(input_str) >= 97 and ord(input_str) <= 122:
            input_str = chr(ord(input_str) - 32)
        print("{}".format(input_str), end="")
    print("")
