import math
def square(a):
    sq = a * a
    if sq % a == 0:
        print(sq)
    else:
        fraction = math.ceil(a)
        print(fraction)

square(9.1)