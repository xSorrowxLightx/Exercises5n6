import math
from operator import truediv


#EXERCISE 1

def hypot(sidea, sideb):
    sqr_ab = sidea**2 + sideb**2
    sidec = math.sqrt(sqr_ab)
    return sidec

print(hypot(3,4))

#EXERCISE 2

def is_between(x, y, z):
    if x > y > z or x < y < z:
        return True
    else:
        return False

print(is_between(3,4,5))

#EXERCISE 3
"""
def ackermann(m, n):
    if m == 0:
        ackermann(m, n-1)
    elif m > 0 and n == 0:
        ackermann(m-1, 1)
    elif m > 0 and n > 0:
        ackermann(m-1, ackermann(m, n-1))
    else:
        pass

ackermann(5, 5)

yeah uh this is beyond me. 
no idea what the heckies he talkin bout
"""

#im callin it here cause i got other chapters to catch up on