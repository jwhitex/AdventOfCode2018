import heapq
from io import StringIO
from collections import defaultdict
from functools import reduce
import itertools

inputs="""Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

(ix_first, ix_then) = 1,7
def arrange(x,y):
    words=y.split()
    first,then=words[ix_first],words[ix_then]
    if first not in x[0]: x[0].append(first)
    if then not in x[0]: x[0].append(then)
    x[1][then].append(first)
    x[1][then] = x[1][then]
    return x

(steps, assembly)=reduce(arrange, [step for step in open("day7.input").read().splitlines()], (list(), defaultdict(list)))
#(steps, assembly)=reduce(arrange, [step for step in StringIO(inputs).read().splitlines()], (list(), defaultdict(list)))

# find the first step that doesn't have a requirement in assembly
def next_step(assembly):
    candidates = []
    for key in assembly:
        if len(assembly[key]) == 0:
            candidates.append(key)
            continue
        for pred in assembly[key]:
            if pred not in iter(assembly):
                candidates.append(pred)
    if len(candidates) == 0: raise Exception()
    return sorted(candidates)[0]

def rm_step(assembly, rm_key):
    for key in assembly.copy():
        if key == rm_key:
            assembly.pop(key)
            continue
        for i in range(0, len(assembly[key])):
            if assembly[key][i] == rm_key:
                assembly[key].pop(i)
                break

# osteps=''
# while len(assembly) != 0:
#     nk = next_step(assembly)
#     rm_step(assembly, nk)
#     osteps+=nk

# pt1
# CQSWKZFJONPBEUMXADLYIGVRHT
# print(osteps)


# pt2
def step2sec(s):
    return ord(s) - 64 + 60  # s is upper

def aany(func, arr):
    for val in arr: 
        if func(val): return True
    return False
def aall(func, arr):
    for val in arr: 
        if not func(val): return False
    return True
def dany(func, d):
    for val in d: 
        if func(d[val]): return True
    return False
def dall(func, d):
    for val in d: 
        if not func(d[val]): return False
    return True

def next_steps(assembly):
    candidates = []
    for key in assembly:
        if len(assembly[key]) == 0:
            candidates.append(key)
            continue
        for pred in assembly[key]:
            if pred not in iter(assembly) and pred not in candidates:
                candidates.append(pred)
    if len(candidates) == 0: raise Exception()
    return sorted(candidates)

def can_offload(c, num_workers, reqs):
    if len(c) == 0: return True
    if len(c) == num_workers: return False
    cur_queued = [e for e, cnt in c.items()]
    for req in reqs:
        if req in cur_queued: return False
    return True

def deplete_worker(workers, total_time):
    while not dany(lambda x: x == 0, workers):
        total_time += 1
        for (e, i) in workers.items():
            workers[e] = i -1
    return (+workers, total_time)

import collections
from copy import deepcopy
num_workers = 5
total_time = 0
oassembly = deepcopy(assembly)
workers = collections.Counter() 
nsteps = []

while len(assembly) != 0:
    if not len(nsteps):
        nsteps = next_steps(assembly)
    nsteps_cache = []
    for i in range(0, len(nsteps)):
        n = nsteps[i]
        if can_offload(workers, num_workers, oassembly[n]):
            workers[n] = step2sec(n)
            rm_step(assembly, n)
        else: nsteps_cache += [n]
    nsteps = nsteps_cache
    if len(nsteps):
        (workers, total_time) = deplete_worker(workers, total_time)
(workers, total_time) = deplete_worker(workers, total_time)

# 914
print(total_time)
        
       
    






