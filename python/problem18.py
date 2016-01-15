#!/usr/bin/env python

import time

def get_results(current, previus):
    results = []
    for i in range(0,len(current)):
        results.append(max(current[i] + previus[i] , current[i] + previus[i+1]))
    return results

def main():
    start_time = time.time()

    triangle = []
    with open('problem18_input.txt') as f:
        for line in f.readlines():
            line_numbers = line.strip().split(' ')
            triangle.append(map(lambda x: int(x), line_numbers))

    height = len(triangle)
    previus_results = []

    levels = range(0,height)
    levels.reverse()

    for i in levels:
        if i == height-1:
            previus_results = triangle[i]
            continue

        previus_results = get_results(triangle[i], previus_results)

    result = previus_results[0]
    stop_time = time.time()

    print "Runtime: " + str(stop_time - start_time)
    print "Maximum sum path: " + str(result)


if __name__ == '__main__':
    main()