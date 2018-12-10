import pandas
import re
from datetime import datetime
from io import StringIO

# DAY 5
import itertools
import functools
import sys

def upper(v):
    if ord(v) > 64 and ord(v) < 91: return v
    if ord(v) > 96 and ord(v) < 123: return chr(ord(v)-32)
    return None

def lower(v):
    if ord(v) > 64 and ord(v) < 91: return chr(ord(v)+32)
    if ord(v) > 96 and ord(v) < 123: return v
    return None

def react(s):   
    if s[0] == s[1]: return False
    if upper(s[0]) == upper(s[1]): return True
    return False

def adjacents(s):
    count = 0
    it1 = itertools.islice(s[0:],0,None,2)
    it2 = itertools.islice(s[1:],0,None,2)
    left = next(it1, None)
    right = next(it2, None)
    while left is not None and right is not None:
        if count % 2 == 0:
            yield left + right
            left = next(it1, None)
        else:
            yield right + left
            right = next(it2, None)
        count += 1

def all_lletters():
    return map(lambda x: chr(x), range(97,123))

def combust(s):
    collapsed=''
    skip_next=False
    for comb in adjacents(s):
        if skip_next:
            skip_next=False
            continue
        if not react(comb):
            collapsed+=comb[0:1]
        else:
            skip_next=True
    if not skip_next:
        collapsed+=s[len(s)-1]
    return collapsed

def filter_icase(s,c):
    ret = []
    for val in itertools.filterfalse(lambda x: upper(x)==upper(c), s):
        ret += [val]
    return ret

def combust_all(pchain):
    res = combust(pchain)
    while True:
        tmp = combust(res)
        if len(res) != len(tmp): res = tmp
        else: break
    return res
    
def poly_stats(pchain):
    for l in all_lletters():
        yield combust_all(filter_icase(pchain,l))

polymer_chain=""
with open("day5.input") as file:
    for line in file:
        polymer_chain=line.rstrip("\r\n")

#polymer_chain='dabAcCaCBAcCcaDA'

#day5 pt1
#print(len(combust_all(polymer_chain)))

#day5 pt2
min_poly_chain = functools.reduce(lambda x,y: x if x<len(y) else len(y), poly_stats(polymer_chain), sys.maxsize) # initialize with sys wordsize
print(min_poly_chain)

