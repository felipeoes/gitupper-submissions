#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    # Split the input string into hours, minutes, and seconds
    hours, minutes, seconds = s[:2], s[3:5], s[6:8]
    
    # If the input time is in PM and the hours is less than 12, add 12 to the hours
    if s[-2:] == 'PM' and hours < '12':
        hours = str(int(hours) + 12)
    
    # If the input time is in AM and the hours is 12, set the hours to 0
    if s[-2:] == 'AM' and hours == '12':
        hours = '00'
    
    # Return the time in 24-hour format
    return f"{hours}:{minutes}:{seconds}"
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
