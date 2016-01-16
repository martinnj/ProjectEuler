#!/usr/bin/env python

import time

def prime_sieve(n):
    """
    Function from:
    https://stackoverflow.com/questions/17773352/python-sieve-prime-numbers
    """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def main():
    start_time = time.time()

    limit = 1000
    for denom in prime_sieve(limit)[::-1]:
        period = 1
        while pow(10, period, denom) != 1:
            period += 1
        if denom-1 == period:
            break

    stop_time = time.time()

    print "Runtime: " + str(stop_time - start_time)
    print "d for longest recurring cycle for 1/d: " + str(denom)

if __name__ == '__main__':
    main()