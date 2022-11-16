#!/bin/python3

"""
Convert decimal to binary
"""

import argparse

from stack import Stack


def dec2bin(dec):
    
    # return 0 if dec is 0
    if dec == 0:
        return 0
    
    # create a class from Stack
    stack = Stack()

    while dec > 0:
        rem = dec % 2
        # push this rem to stack
        stack.push(rem)

        dec = dec // 2
    
    bin = ""
    while not stack.is_empty():
        bin += str(stack.pop())
    
    return bin

if __name__ == "__main__":
    msg = "Program to convert integer values to binary using stack."
    parser = argparse.ArgumentParser(
        description=msg,
        epilog="Example: ./dec2bin.py -n 10"
    )
    parser.add_argument("-n", "--number",help="integer to convert to binary", type=int)
    args = parser.parse_args()
    print(dec2bin(args.number))


