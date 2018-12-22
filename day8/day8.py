import itertools
from io import StringIO
from queue import LifoQueue

inputs = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

#data = [int(v) for v in StringIO(inputs).read().split(' ')]
data = [int(v) for v in open("day8.input").read().split(' ')]

def parse_packet(idata, lifoq_children, tc_metadata):
    if not lifoq_children.empty():
       c_childn_level = q.get()
    else: c_childn_level = 1
    for i in range(0, c_childn_level):
        c_childn = next(idata, None)
        if c_childn is None: break
        # know iter not empty
        c_metad = next(idata) # know has value
        if c_childn > 0:
            lifoq_children.put(c_childn)
            tc_metadata += parse_packet(idata, lifoq_children, 0)
        for i in range(0, c_metad):
            md = next(idata)
            tc_metadata += md
    return tc_metadata

# idata = iter(data)
# q = LifoQueue()
# tc_metadata = parse_packet(idata, q, 0)
# print(tc_metadata)

# pt2
def parse_packet_pt2(idata, lifoq_children):
    level_values = []
    if not lifoq_children.empty():
       c_childn_level = q.get()
    else: c_childn_level = 1
    for i in range(0, c_childn_level):
        child_values = []
        tc_metadata = 0
        c_childn = next(idata, None)
        if c_childn is None: break
        # know iter not empty
        c_metad = next(idata)
        if c_childn > 0:
            lifoq_children.put(c_childn)
            # list of values from children
            child_values = parse_packet_pt2(idata, lifoq_children)
        for i in range(0, c_metad):
            md = next(idata)
            if c_childn == 0:
                tc_metadata += md
            else:
                if md == 0: continue
                if len(child_values) >= md:
                    tc_metadata += child_values[md-1]
        level_values += [tc_metadata]
    return level_values

idata = iter(data)
q = LifoQueue()
tc_metadata = parse_packet_pt2(idata, q)[0]
print(tc_metadata)
