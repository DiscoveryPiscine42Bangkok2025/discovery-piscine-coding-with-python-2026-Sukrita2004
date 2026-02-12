#!/usr/bin/env python3

import sys

def shrink(c):
    print(c[:8])
def enlarge(c):
    while len(c) < 8:
        c += "Z"
    print(c)
if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)