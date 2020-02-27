#!/usr/bin/env python3
import sys
import os
import random
import json
from copy import deepcopy
import pathlib

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

code_file = os.path.join(pathlib.Path(__file__).parent.absolute(), 'city_codes.json')
with open(code_file, 'r') as f:
    CITY_CODES = json.load(f)
    FLATTERN_CODES = []
    for cities in CITY_CODES.values():
        for codes in cities.values():
            FLATTERN_CODES.extend(codes)
    

class INID:
    def __init__(self, inid):
        if not isinstance(inid, str) or len(inid) not in (9,10):
            raise ValueError("Bad INID ({inid})")
        self._value = inid

    @property
    def value(self):
        if len(self._value) == 9:
            return generate_id(self._value)
        return self._value

    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.__str__()
    
    def is_valid(self):
        return check_id(self.value)


class INID_RANGE:
    def __init__(self, start='000000', end='999999', city_codes=None):
        self._start = start
        self._end = end
        self._city_codes = city_codes
        self._current = int(self._start)
        self._stop = int(self._end)
        self._current_city = None 
        if self._city_codes:
            self._cities = deepcopy(self._city_codes)
        else:
            self._cities = deepcopy(FLATTERN_CODES)


    def __iter__(self):
        self._current = int(self._start)
        if self._city_codes:
            self._cities = deepcopy(self._city_codes)
        else:
            self._cities = deepcopy(FLATTERN_CODES)
        return self
 
    def __next__(self):

        if not self._current_city:
            try:
                self._current_city = self._cities.pop(0)
            except IndexError as e:
                raise StopIteration()

        if self._current <= self._stop:
            c = self._current
            self._current += 1
            return INID(f"{self._current_city}{c:06d}")
        else:
            self._current_city = None
            self._start = int(self._start) 
            












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
