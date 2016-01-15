#!/usr/bin/env python

import time
import math



def main():
    start_time = time.time()
    long_num = long(2)**1000
    long_str = str(long_num)
    final_sum = long(0)

    for ch in long_str:
        final_sum += long(ch)

    stop_time = time.time()

    print "Runtime: " + str(stop_time - start_time)
    print "Sum of digits in power: " + str(final_sum)

if __name__ == '__main__':
    main()