# Read an integer N.
# Without using any string methods, try to print the following: 123 ... N
# Note that "..." represents the values in between.

from __future__ import print_function

n = int(raw_input('Give a number: '))

for x in range(1,n+1):
    print(x, sep=' ', end='')