#!/usr/bin/python3

def read_file(filename=""):
    """ function that reads a text file and prints it to a standard output """

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
