#!/usr/bin/env python

import time

def collatz_len(n):
    if n == 1:
        return 1
    if (n % 2) == 0:
        return 1 + collatz_len(n/2)
    else:
        return 1 + collatz_len(3*n+1)

def main():
    start_time = time.time()
    longest_len = 0
    longest_num = 0
    for n in range (1,1000001):
        l = collatz_len(n)
        if l > longest_len:
            longest_len = l
            longest_num = n

    stop_time = time.time()

    print "Runtime: " + str(stop_time - start_time)
    print "Number: " + str(longest_num)
    print "Collatz sequence length: " + str(longest_len)
    


if __name__ == '__main__':
    main()