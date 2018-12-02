import itertools

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

accounting=dict({(2,0),(3,0)})
for i in range(0, len(inputs)):
    a,b=False,False
    for val in unique_everseen(inputs[i]):
        count=quantify(inputs[i], lambda x: x==val)
        if count == 2 and not a:
            a = True
            accounting[count]+=1
        if count == 3 and not b:
            b = True
            accounting[count]+=1
        if a and b:
            break
print("Checksum: {}".format(accounting[2]*accounting[3]))

# 5750


