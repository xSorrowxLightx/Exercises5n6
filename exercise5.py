#EXERCISE 1

from time import time
time = time()

def timesince (time):
    days = time // (24 * 3600)
    years = days //365
    remainder = days % 365
    print(f"It's been {int(days)} days, or {int(years)} years and {int(remainder)} days since January 1st, 1970.")

timesince(time)

#EXERCISE 2

def istriangle(l1, l2, l3):
    a,b,c = l1,l2,l3
    if a + b > c and a + c > b and b + c > a:
        print("It's a triangle!")
    else:
        print("It's not a triangle.")

istriangle(4,5,7)

#EXERCISE 3

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3,0)

"""
okay it looks like it wants me to write this out. 
what happens is that at the start n is NOT 0 so it minuses 1
from the original n and adds n to s, which i guess
in this case is like an output. because its a recursive function,
this continues until n == 0, at which point it prints s which
is now equal to n times how many times it had to loop
(which is also n)
so basically,
first loop = s + 3 = 3
second loop = s + 2 = 5
third loop = s + 1 = 6
and then the loop finishes cause n == 0, meaning it prints s,
which is now 6!
"""

#EXERCISE 4

import turtle
from turtle import forward, left, right, back

def draw(length):
    angle = 50
    factor = 0.6

    if length > 5:
        forward(length)
        left(angle)
        draw(factor * length)
        right(2 * angle)
        draw(factor * length)
        left(angle)
        back(length)
    else:
        pass

"""
okay it wants me to write this out too.
so if length is less than 5, itll draw a picture?
tbh i havent a clue what kind of picture. i think the draw
parts are going to be diagonal angles? is it gonna be a octagon
or something? or a hexagon. imma go with hexagon.
"""

draw(20)

"""
uh.... it just kinda flashes open for a second.
i only saw a tiny bit of movement

EDIT: OH I MADE THE NUMBER HIGHER ITS FRACTALLLSS
"""

#EXERCISE 5 and 6

# i havent the slightest on how to even begin these
# skipping