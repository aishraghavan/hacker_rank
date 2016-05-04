"""
Plus Minus

https://www.hackerrank.com/challenges/plus-minus

Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10−410−4 are acceptable.

Input Format

The first line contains an integer, NN, denoting the size of the array.
The second line contains NN space-separated integers describing an array of numbers (a0,a1,a2,…,an−1)(a0,a1,a2,…,an−1).

Output Format

You must print the following 33 lines:

A decimal representing of the fraction of positive numbers in the array.
A decimal representing of the fraction of negative numbers in the array.
A decimal representing of the fraction of zeroes in the array.
Sample Input

6
-4 3 -9 0 4 1
Sample Output

0.500000
0.333333
0.166667
Explanation

There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The respective fractions of positive numbers, negative numbers and zeroes are 3/6=0.50000036=0.500000, 2/6=0.33333326=0.333333 and 1/6=0.16666716=0.166667, respectively.

"""

#!/bin/python

import sys
n = 0
a = []


def calculate_fraction():
    if n != len(a):
        return
    positive = negative = zero = 0
    for ele in a:
        if ele > 0:
            positive += 1
        elif ele < 0:
            negative += 1
        else:
            zero += 1
    print positive/float(n)
    print negative/float(n)
    print zero/float(n)

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
calculate_fraction()
