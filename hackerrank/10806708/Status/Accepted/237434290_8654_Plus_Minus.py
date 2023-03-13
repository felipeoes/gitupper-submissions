#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    total = len(arr)
    positive = 0
    negative = 0
    zeros = 0
    
    for number in arr:
        if number > 0:
            positive+=1
        elif number < 0:
            negative +=1
        else:
            zeros+=1
    print(positive / total)
    print(negative / total)
    print(zeros / total)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
