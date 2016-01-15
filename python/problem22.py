#!/usr/bin/env python

import time
import string

def main():
    start_time = time.time()

    names = []
    name_scores = []

    with open('problem22_input.txt') as f:
        for line in f.readlines():
            names = line.strip().replace("\"","").split(",")

    names.sort()

    for name in names:
        name_value = 0
        for letter in name:
            name_value += string.uppercase.index(letter) + 1
        name_place = names.index(name) + 1
        name_scores.append(name_value * name_place)

    name_score_sum = sum(name_scores)
    stop_time = time.time()

    print "Runtime: " + str(stop_time - start_time)
    print "Sum of all name scores: " + str(name_score_sum)


if __name__ == '__main__':
    main()