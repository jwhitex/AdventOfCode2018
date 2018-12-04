import re
import itertools
import numpy as np

inputs=[]
with open("day3.test.input") as file:
    for line in file:
        lclean = line.rstrip("\r\n")
        if lclean == "":
            continue
        inputs+=[lclean]

class Fabric():
    def __init__(self,bid,dw,dh,w,h):
        self.bid=int(bid)
        self.dw=int(dw)
        self.dh=int(dh)
        self.w=int(w)
        self.h=int(h)

pinputs = []
max_height=0
max_width=0
for i in range(0, len(inputs)):
    m = re.match(r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$", inputs[i])
    bid,dw,dh,w,h=m.group(1,2,3,4,5)
    f=Fabric(bid,dw,dh,w,h)
    pinputs+=[f]
    if f.dw + f.w > max_width:
        max_width=f.dw + f.w
    if f.dh + f.h > max_height:
        max_height=f.dh + f.h

mat_sum = np.zeros((max_width,max_height))
mats = []
for f in pinputs:
    mat=np.zeros((max_width, max_height))
    for i in range(0,f.w):
        for j in range(0,f.h):
            mat[f.dw+i,f.dh+j] = 1
    mats+=[mat]

# sum fabric dimensions
for i in range(0, len(mats)):
    mat_sum += mats[i]

# pt1
overlaps = mat_sum[np.where( mat_sum > 1 )]
print(len(overlaps))
