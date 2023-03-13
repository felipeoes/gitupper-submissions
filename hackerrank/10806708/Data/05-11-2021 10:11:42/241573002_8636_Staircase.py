#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    spaces = n
    
    for i in range(n):
        spaces -= 1
        print(' ' * spaces + '#' * (i+1))
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
