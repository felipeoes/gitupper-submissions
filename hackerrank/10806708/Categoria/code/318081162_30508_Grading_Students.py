#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def round_grade(grade: int) -> int:
    if grade < 38:
        return grade
    else:
        next_multiple_five = grade + (5 - grade) % 5
        grade_diff = next_multiple_five - grade
        
        if grade_diff < 3:
            return next_multiple_five
        
        return grade
            

def gradingStudents(grades):
    for index in range(len(grades)):
        grades[index] = round_grade(grades[index])
        
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
