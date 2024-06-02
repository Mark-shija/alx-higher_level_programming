#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    Answer = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            Answer = Answer + int(arg)

    print(Answer)
