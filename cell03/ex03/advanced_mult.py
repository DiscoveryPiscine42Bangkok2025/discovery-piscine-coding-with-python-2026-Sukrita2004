#!/usr/bin/env python3

x = 0
while x < 11:
    j = 0
    print(f"Table de {x}: ", end=" ")
    while j < 11:
        print(f"{x*j} ", end=" ")
        j+=1
    print()
    x+=1