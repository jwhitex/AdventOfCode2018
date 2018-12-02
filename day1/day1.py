#!/usr/bin/env python
f = 0
with open("day1.input") as file:
    for line in file:
        cng = int(line.rstrip("\n\r"))
        f += cng
print(f)
