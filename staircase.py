"""
https://www.hackerrank.com/challenges/staircase


Your teacher has given you the task of drawing a staircase structure. Being an expert programmer, you decided to make a program to draw it for you instead. Given the required height, can you print a staircase as shown in the example?

Input
You are given an integer NN depicting the height of the staircase.

Output
Print a staircase of height NN that consists of # symbols and spaces. For example for N=6N=6, here's a staircase of that height:

     #
    ##
   ###
  ####
 #####
######
Note: The last line has 0 spaces before it.
"""

#!/bin/python

import sys


def test_stairs(n):
  if n<1:
    return
  for index in range(n-1,-1,-1):
    last_index = n-index
    str =' '*index
    temp_str = '#'*last_index
    str += temp_str
    print str


n = int(raw_input().strip())
test_stairs(n)
