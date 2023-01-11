#!/usr/bin/python3
""" Program that Read n lines """


def read_lines(filename="", nb_lines=0):
    """ function that reads n lines of a text file (UTF8) and
    prints it to stdout """
    count = 0
    with open(filename, encoding='utf-8') as f:
        if (nb_lines <= 0):
            print(f.read(), end='')
        for line in f:
            if (count < nb_lines):
                print(line, end='')
                count += 1
