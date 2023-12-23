# get to the other side of the road
# "currently" located at position "X" and wants to get to a position "greater than or equal to Y"  X <= Y
# Count the "minimal" number of jumps
# return 3
from math import ceil

# 44% : int(dist/D)+1, 100% : ceil
def solution(X, Y, D):
    # return ceil(dist/D)
    dist = Y-X
    if dist % D == 0:
        return dist//D
    else:  # > 0
        return dist//D + 1
    