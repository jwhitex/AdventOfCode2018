from functools import reduce
import math

grid_dim = 301

def digit_of_int(num,digit):
    s = str(abs(num))
    return 0 if len(s) < digit else int(s[-digit])

def powerlevels(gridserial):
    # Correct 2d array creation. [[0]*301]*301 is WRONG.
    # In that instance each row references the same array!
    pwr_levels = [[0]*grid_dim for i in range(0,grid_dim)]
    #print(pwr_levels)
    for y in range(1,grid_dim):
        for x in range(1,grid_dim):
            rackid_ix = x + 10
            pl = rackid_ix*y
            pl += gridserial
            pl *= rackid_ix
            pl = digit_of_int(pl,3)
            pl -= 5
            pwr_levels[y][x] = pl
    return pwr_levels

def max_fuel_cell_3x3(pls):
    pl_sum_max = 0
    tlfuelcell_max = (0,0)
    for y in range(1,grid_dim-3):
        for x in range(1,grid_dim-3):
            pl_sum = sum(pls[y][x:x+3]) \
                + sum(pls[y+1][x:x+3]) \
                + sum(pls[y+2][x:x+3])
            if pl_sum > pl_sum_max:
                pl_sum_max = pl_sum
                tlfuelcell_max = (x,y)
    return tlfuelcell_max

# BEGIN PT2 TRY
def sum_pwr(y1, y2, x1, x2, plvs):
    pl_sum = 0
    for y in range(y1, y1+y2):
        pl_sum += sum(plvs[y][x1:x1+x2])
    return pl_sum

# too slow
def max_fuel_cell_grid(pls):
    pl_sum_max = 0
    edge_len = grid_dim
    while True:
        upper_ix = grid_dim+2-edge_len
        for y in range(1,upper_ix):
            for x in range(1,upper_ix):
                pl_sum = sum_pwr(y, edge_len, x, edge_len, pls)
                print("{},{} {} x {} : {}".format(x,y,edge_len,edge_len,pl_sum))
                if pl_sum > pl_sum_max:
                    pl_sum_max = pl_sum
                    tlfuelcell_max = '{},{},{}'.format(x,y,edge_len)
        edge_len -= 1
        if edge_len == 1: break
        print(edge_len)
    return tlfuelcell_max
# END

# BEGIN PT2 2
def sum_pwr_outer_level(x,y,edge_size,ones_grid):
    pwr_sum = 0
    for x1 in range(x, x+edge_size):
        pwr_sum += ones_grid[y+edge_size-1][x1]
    for y1 in range(y, y+edge_size-1):
        pwr_sum += ones_grid[y1][x+edge_size-1]
    return pwr_sum

def power_level_at_fuel_cell(x,y,edge_size, pwrs2_grids):
    pl_sum = pwrs2_grids[edge_size-2][y][x]
    pl_sum += sum_pwr_outer_level(x, y, edge_size, pwrs2_grids[0])
    #debug_print(x,y,edge_size,pwrs2_grids, pl_sum)
    return pl_sum

def debug_print(x,y,edge_size,pwrs2_grids, pl_sum):
    # all this because switched x and y in an array index :'(
    if x==232 and y ==251:
        temp_sum = pwrs2_grids[edge_size-2][y][x]
        print('edge_size {} sum was: {}'.format(str(edge_size), str(temp_sum)))

        print('alg says sum is: {}'.format(str(pl_sum)))
        grid = [[0]*edge_size for i in range(0,edge_size+1)]
        for y1 in range(edge_size):
            for x1 in range(edge_size):
                grid[y1][x1] = pwrs2_grids[0][y+y1][x+x1]
        easy_sum = 0
        for i in range(edge_size):
            easy_sum += sum(grid[i])
            print("{}, sum: {}".format(str(grid[i]), sum(grid[i])))
        print('clearly sum is: {}'.format(str(easy_sum)))
    else: return

def max_fuel_cell_any(pls):
    pl_sum_max = 0
    gs_sums = [[[pls[i][j] for j in range(0,grid_dim)] for i in range(0,grid_dim)]]
    for gs in range(2, grid_dim):
        upper_ix = grid_dim - gs + 1
        if __debug__:
            print(upper_ix)
            print(gs)
        gs_sum_new = [[0]*grid_dim for i in range(0,grid_dim)]
        for y in range(1,upper_ix):
            for x in range(1,upper_ix):
                pl_sum = power_level_at_fuel_cell(x,y,gs,gs_sums)
                gs_sum_new[y][x] = pl_sum
                if pl_sum > pl_sum_max:
                    pl_sum_max = pl_sum
                    tlfuelcell_max = '{},{},{} : {}'.format(x,y,gs, pl_sum_max)
        gs_sums += [gs_sum_new]
    return tlfuelcell_max

#print(powerlevels(8)[5][3])
#print(powerlevels(57)[79][122])
#print(powerlevels(39)[196][217])
#print(powerlevels(71)[153][101])
#print(max_fuel_cell_3x3(powerlevels(18)))
#print(max_fuel_cell_3x3(powerlevels(42)))
#print(max_fuel_cell_3x3(powerlevels(3999)))

# Expected 90,269,16 : 113
#print(pwr_levels_yo(powerlevels(18)))
# 90,269,16 : 115

# Expected 232,251,12 : 119
#print(pwr_levels_yo(powerlevels(42)))
# 232,251,12  : 129

#227,222,27 : 256

print(max_fuel_cell_any(powerlevels(3999)))
quit()

