#!/usr/bin/env python

import time
import datetime

def main():
    start_time = time.time()

    sundays = 0
    for year in xrange(1901, 2001):
        for month in xrange(1, 13):
            d = datetime.date(year, month, 1)
            if d.weekday() == 6:
                sundays = sundays + 1

    stop_time = time.time()

    print "Runtime: " + str(stop_time - start_time)
    print "Sundays on first of the month: " + str(sundays)

if __name__ == '__main__':
    main()