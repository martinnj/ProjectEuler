#!/usr/bin/env python

import time
from itertools import permutations

def main():
    start_time = time.time()

    lst = [0,1,2,3,4,5,6,7,8,9]
    prm_lst = list(permutations(lst))
    prm_lst.sort()
    res = reduce(lambda rst, d: rst * 10 + d, prm_lst[999999])

    stop_time = time.time()

    print "Runtime: " + str(stop_time - start_time)
    print "1,000,000th permutation: " + str(res)

if __name__ == '__main__':
    main()