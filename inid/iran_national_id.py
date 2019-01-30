#!/usr/bin/env python3
import sys
import random


def generate_id(prefix=''):
    if not isinstance(prefix, str):
        prefix = str(prefix)

    if 1 > len(prefix) > 9:
        raise ValueError("Invalid prefix, prefix must has 1 to 9 digits")
    
    nid = "{:s}{:s}".format(prefix, ''.join([str(random.randint(0,9)) for _ in range(9-len(prefix))]))
    nsum = 0
    for p in range(10, 1, -1):
        nsum += int(nid[10 - p]) * p
    r = nsum % 11
    checksum = r if r < 2 else 11 - r
    return "{:s}{:d}".format(nid, checksum)


def check_id(nid):
    if not isinstance(nid, str):
        nid = str(nid)

    if 1 > len(nid) > 9:
        raise ValueError("Invalid prefix, prefix must has 1 to 9 digits")

    nsum = 0
    for p in range(10, 1, -1):
        nsum += int(nid[10 - p]) * p
    r = nsum % 11
    checksum = r if r < 2 else 11 - r
    return checksum == int(nid[-1])


def main():
    inp = input("Nid or Part: ")
    if len(inp) < 10:
        print(generate_id(inp))
    elif len(inp) == 10:
        print("Correct" if check_id(inp) else "Incorrect")
    else:
        print("Invalid digit count", file=sys.stderr)


if __name__ == "__main__":
    main()
