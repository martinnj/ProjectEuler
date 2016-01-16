#!/usr/bin/env python

import time
from math import sqrt

def d(N):
    return sum(n for n in xrange(1, int(N/2.0)+1) if N % n == 0)

def main():
    start_time = time.time()

    limit = 28123
    asum = 0
    abundants = set()

    for n in range(1, limit):
        if d(n) > n:
            abundants.add(n)
        if not any( (n-a in abundants) for a in abundants ):
            asum += n

    stop_time = time.time()

    print "Runtime: " + str(stop_time - start_time)
    print "Sum of positive intergers that can't be created by abundant numbers: " + str(asum)

if __name__ == '__main__':
    main()