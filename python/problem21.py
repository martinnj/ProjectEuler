#!/usr/bin/env python

import time
from math import sqrt

def d(N):
    return sum(n for n in xrange(1, int(N/2.0)+1) if N % n == 0)

def main():
    start_time = time.time()
    divsum = dict()
    final_sum = 0

    # Precompute all the sum divisors.
    for i in xrange(1,10000):
        divsum[i] = d(i)

    for i in xrange(1,10000):
        for j in xrange(1,i):
            if divsum[i] == j and divsum[j] == i:
                final_sum += i + j


    stop_time = time.time()

    print "Runtime: " + str(stop_time - start_time)
    print "Sum of amicable numbers below 10000: " + str(final_sum)

if __name__ == '__main__':
    main()