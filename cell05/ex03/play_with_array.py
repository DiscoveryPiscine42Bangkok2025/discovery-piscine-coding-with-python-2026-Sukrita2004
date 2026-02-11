#!/usr/bin/env python3


ori_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

for v in ori_array:
    if v > 5:
        if v + 2 not in new_array:
            new_array.append(v + 2)
