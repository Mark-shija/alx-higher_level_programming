#!/usr/bin/python3
for alphabet_char in range(97, 123):
    if chr(alphabet_char) not in ['q', 'e']:
        print("{}" .format(chr(alphabet_char)), end='')
