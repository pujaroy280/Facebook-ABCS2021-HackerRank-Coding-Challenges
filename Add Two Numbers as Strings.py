#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compute_sum' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING x
#  2. STRING y
#

def compute_sum(x, y):
    # Write your code here 
    # Before proceeding further,
    # make sure length of str2 is larger.
    if (len(x) > len(y)):
        t = x;
        x = y;
        y = t;
 
    # Take an empty string for
    # storing result
    str = "";
 
    # Calculate length of both string
    n1 = len(x);
    n2 = len(y);
 
    # Reverse both of strings
    x = x[::-1];
    y = y[::-1];
 
    carry = 0;
    for i in range(n1):
         
        # Do school mathematics, compute
        # sum of current digits and carry
        sum = ((ord(x[i]) - 48) +
              ((ord(y[i]) - 48) + carry));
        str += chr(sum % 10 + 48);
 
        # Calculate carry for next step
        carry = int(sum / 10);
 
    # Add remaining digits of larger number
    for i in range(n1, n2):
        sum = ((ord(y[i]) - 48) + carry);
        str += chr(sum % 10 + 48);
        carry = (int)(sum / 10);
 
    # Add remaining carry
    if (carry):
        str += chr(carry + 48);
 
    # reverse resultant string
    str = str[::-1];
 
    return str;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    input_x = input()

    input_y = input()

    solution = compute_sum(input_x, input_y)

    fptr.write(solution + '\n')

    fptr.close()
