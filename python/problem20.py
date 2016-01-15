#!/usr/bin/env python

import time

def fact(n):
    ns = range(1,n+1)
    return reduce(lambda x, y: x*y, ns, 1)

def main():
    start_time = time.time()

    final_sum = 0
    for ch in str(fact(100)):
        final_sum += int(ch)

    stop_time = time.time()

    print "Runtime: " + str(stop_time - start_time)
    print "Sum of digits in 100!: " + str(final_sum)

if __name__ == '__main__':
    main()