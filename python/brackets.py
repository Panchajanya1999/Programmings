#!/bin/python3

"""
Bracket Matching
Determine whether a given string of parantheses is properly nested.
"""

from stack import Stack
import argparse


def check_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_paren_balanced(string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(string) and is_balanced:
        paren  = string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not check_match(top, paren):
                    is_balanced = False
        index += 1
    
    if s.is_empty() and is_balanced:
        return True
    else:
        return False

if __name__ == "__main__":
    msg = "Program checks whether a string has balanced usage of parantheses."
    parser = argparse.ArgumentParser(
        prog = "brackets",
        description=msg,
        epilog = "Program Writen in Python 3.11"
    )
    parser.add_argument("string", metavar="S",type = str, help="String to check for balanced parantheses.")
    args = parser.parse_args()
    print(args.string)
    print(is_paren_balanced(args.string))
