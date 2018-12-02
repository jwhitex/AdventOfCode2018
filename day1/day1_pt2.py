#!/usr/bin/env python

def runSim(fsum, series, fdict):
    for i in range(0,len(series)):
        fsum += series[i]
        if fsum in fdict:
            return (True, fsum)
        fdict[fsum] = None
    return (False, fsum)

fin=[]
with open("day1.input") as file:
    for line in file:
        fin+=[int(line.rstrip("\n\r"))]

fdict=dict({ 0:None})
fsum = 0
while True:
    found,fsum = runSim(fsum, fin, fdict)
    if found:
        break
print(fsum)
