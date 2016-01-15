#!/usr/bin/env python

from math import sqrt 
import time
 
def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))
        
def main():
    start_time = time.time()

    counter = 0
    TriangleNumber = 0

    while True:
        counter += 1
        TriangleNumber += counter
        if len(factors(TriangleNumber)) > 500:
            stop_time = time.time()
            print "Runtime: " + str(stop_time - start_time)
            print "Triangle number: " + str(TriangleNumber)
            exit(0)
         
if __name__ == '__main__':
    main()