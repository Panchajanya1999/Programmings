#!/bin/python3

"""
Reverse a string using a stack.
"""
import argparse
from stack import Stack

def reverse_string(string):
    stack = Stack()

    for char in range(len(string)):
        stack.push(string[char])
    
    reverse = ""
    while not stack.is_empty():
        reverse += stack.pop()
    
    return reverse

if __name__ == "__main__":
    msg = "Program to reverse a string via stack."
    parser = argparse.ArgumentParser(
        description=msg,
        epilog="Example: ./reverse_string.py madaM"
    )
    parser.add_argument("string", metavar="S",type = str, help="String for reversal.")
    args = parser.parse_args()
    print(reverse_string(args.string))

