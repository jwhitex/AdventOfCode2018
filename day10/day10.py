from io import StringIO
import re, sys
import numpy as np
import itertools
import string
import time
from collections import defaultdict
from functools import partial


inputs="""position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
"""

def getcords(line):
    line = ''.join(filter(lambda x: x in string.printable, line ))
    m = re.match(r".*<([\-\s]*\d+),([\-\s]*\d+)>.*<([\-\s]*\d+),([\-\s]*\d+)>.*", line)
    (px,py,vx,vy)=m.groups()
    return [[int(px),int(py)],[int(vx),int(vy)]]

#data = [getcords(v) for v in StringIO(inputs).read().splitlines()]
data = [getcords(v) for v in open("day10.input").read().splitlines()]
position, velocity = np.hsplit(np.array(data),2)
position = np.reshape(np.ravel(position), (position.shape[0], 2))
velocity = np.reshape(np.ravel(velocity), (velocity.shape[0], 2))

def term_write(to_write):
    try:
        raw = sys.stdout
        raw.write(to_write)
        raw.flush()
    except IOError as ex:
        print (ex.message)
def print_arbitrary_sequence(iteration, filler, width=100):
    fill=StringIO()
    max_filler_print=min(iteration+1, len(filler))
    for i in range(0, max_filler_print):
        fill.write(filler[i])
    bar = fill.getvalue() + ' ' * (width - max_filler_print)
    fill.close()
    s = StringIO()
    s.write('\r%s' % bar)
    to_write = s.getvalue()
    s.close()
    term_write(to_write)

def print_cool(s, delay=None):
    windowlen = 100
    for j in range(0, len(s)):
        print_arbitrary_sequence(j, s, windowlen)
        if delay is not None: time.sleep(delay)

def print_cool_arr(arr):
    for i in range(0, len(arr)):
        msg=list(arr[i])
        print_cool(msg, 0.001)
        print("")
    print("")

def min_max(itr):
    minv = next(itr,None)
    if minv is None: return None
    from copy import copy
    maxv = copy(minv)
    for i in itr:
        if i > maxv:
            maxv = i
            continue
        if i < minv:
            minv = i
    return (minv, maxv)

def build_matrix(data):
    good_length = 400
    good_message_len = 100
    (minx,maxx) = min_max(map(lambda x: x[0], data))
    offsetx = abs(minx) if minx < 0 else 0
    if maxx+offsetx +1>good_length: return None
    d = defaultdict(partial(np.full,maxx+offsetx+1,ord('.')))
    for i in range(0, len(data)):
        d[data[i][1]][data[i][0]+offsetx] = ord('#')
    # have to scale the thing..
    message_start = minx if minx > 0 else 0
    ad = [d[i][message_start:] for i in sorted(d)]
    if len(ad[0]) < good_message_len: return ad
    return None

seconds = 0
min_len = 10000
try:
    while True:
        position = position + velocity
        seconds += 1
        print_cool("Second: {}".format(str(seconds)))
        mtx = build_matrix(position)
        if mtx is None: continue
        # message probably fits on screen
        if len(mtx[0]) < min_len: min_len = len(mtx[0])
        if len(mtx[0]) > min_len:
            print_cool(" "*20)
            print()
            break
        print()
        pretty = [''.join(map(chr,i)) for i in mtx]
        print_cool_arr(pretty)

except KeyboardInterrupt:
    print()
    quit(0)


