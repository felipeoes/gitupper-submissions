#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    pdiag_sum = 0
    sdiag_sum = 0
    j = len(arr) - 1
    
    for i in range(len(arr)):
        pdiag_sum += arr[i][i]
        sdiag_sum += arr[i][j]
        j-=1
            
        
    return abs(pdiag_sum - sdiag_sum)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
