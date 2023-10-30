from ast import AsyncWith
from cmath import sqrt
import math


natural_number_range = 1000
natural_squares = {}

for i in range(1, natural_number_range+1):
    natural_squares[i] = i*i

abc = 1000
current_sum = 0
for a in range(1, abc+1):
    for b in range(1, abc+1):
        aSquared = natural_squares[a]
        bSquared = natural_squares[b]
        cSquared = aSquared + bSquared

        sqrtA = math.sqrt(aSquared)
        sqrtB = math.sqrt(bSquared)
        sqrtC = math.sqrt(cSquared)
        if (sqrtA + sqrtB + sqrtC) == 1000:
            if(sqrtA < sqrtB and sqrtB < sqrtC):
                print(sqrtA * sqrtB * sqrtC)

        # if c in natural_squares:
        #    print()
        # for c in range(1, b):
        #    current_sum = a+b+c
        #   aSquared = natural_squares[a]
        #   bSquared = natural_squares[b]
        #    cSquared = natural_squares[c]
        #    if((aSquared + bSquared) == cSquared):
        #        if((a+b)==c):
        #            print()
