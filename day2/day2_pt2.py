import itertools
import functools

inputs=[]
with open("day2.input") as file:
    for line in file:
        inputs+=[line.rstrip("\r\n")]

def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in itertools.filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element

def quantify(iterable, pred=bool):
    "Count how many times the predicate is true"
    return sum(map(pred, iterable))

def diffcount(vec1, vec2):
    return sum(map(lambda a,b: 0 if a == b else 1, vec1, vec2))

def alike(vect1, vect2):
    for i in range(0, min(len(vect1),len(vect2))):
        if vect1[i] == vect2[i]:
            yield vect1[i]

print(len(inputs))
candidates=[]
for i in range(0, len(inputs)):
    a,b=False,False
    for val in unique_everseen(inputs[i]):
        count=quantify(inputs[i], lambda x: x==val)
        if count == 2 or count == 3:
            candidates += [inputs[i]]
            break

pfabids=None
for i in range(0, len(candidates)):
    for j in range(0, len(candidates)):
        if i == j: continue
        if diffcount(candidates[i],candidates[j]) == 1:
            pfabids=(candidates[i],candidates[j])
            break
    if pfabids is not None: break


boxid = functools.reduce(lambda x,y: x+y,alike(pfabids[0],pfabids[1]))
print(boxid)

