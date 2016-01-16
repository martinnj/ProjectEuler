#!/usr/bin/env python

import time

def fib(i, fib_dict):
    return fib_dict[i-1] + fib_dict[i-2]

def main():
    start_time = time.time()

    fibs = dict()
    fibs[1] = 1
    fibs[2] = 1

    i = 3
    while True:
        fibi = fib(i, fibs)
        if len(str(fibi)) < 1000:
            fibs[i] = fibi
            i += 1
            continue
        break


    

    stop_time = time.time()

    print "Runtime: " + str(stop_time - start_time)
    print "Index of first Fibonacci number with 1000 digits: " + str(i)

if __name__ == '__main__':
    main()