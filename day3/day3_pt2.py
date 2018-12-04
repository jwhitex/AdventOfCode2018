import re
import itertools
import numpy as np

inputs=[]
with open("day3.input") as file:
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
        self.mtx = None


#d = dict()
pinputs = []
max_height=0
max_width=0
for i in range(0, len(inputs)):
    m = re.match(r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$", inputs[i])
    bid,dw,dh,w,h=m.group(1,2,3,4,5)
    #d[bid] = dict(pos=(dw,dh),size=(w,h))
    f=Fabric(bid,dw,dh,w,h)
    pinputs+=[f]
    if f.dw + f.w > max_width:
        max_width=f.dw + f.w
    if f.dh + f.h > max_height:
        max_height=f.dh + f.h

mat_sum = np.zeros((max_width,max_height))
mats = []
for f in pinputs:
    f.mtx=np.zeros((max_width, max_height))
    for i in range(0,f.w):
        for j in range(0,f.h):
            f.mtx[f.dw+i,f.dh+j] = 1
    mats+=[f]


def mtxfromdim(cubes):
    l = len(cubes[0])
    fab_plan = np.zeros((max_width, max_height))
    for i in range(0,l):
        fab_plan[cubes[0][i],cubes[1][i]]=1
    return fab_plan

# sum fabric dimensions
for i in range(0, len(mats)):
    mat_sum += mats[i].mtx
fab_plan = mtxfromdim(np.where( mat_sum == 1 ))

for i in range(0, len(mats)):
    comb = fab_plan + mats[i].mtx
    #print(comb)
    overlap = np.where( comb > 1 )
    candidate = mtxfromdim(overlap)
    res = np.equal(mats[i].mtx,candidate)
    if res.all():  # all values of matrix are true
        print(mats[i].bid)
        break

# don't judge
# (╯°□°)╯︵ ┻━┻
