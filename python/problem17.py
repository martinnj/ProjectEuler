#!/usr/bin/env python

import time

def spell(n, num_to_str):
    word = []
    while n > 0:
        for num in num_to_str:
            if num[0] <= n:
                div = n / num[0]
                n = n % num[0]
                if num[2]:
                    word.append(' '.join(spell(div, num_to_str)))
                word.append(num[1])
                if num[2] and n:
                    word.append(num[2])
                break
    return word

def main():
    num_to_str = [
        (   1, 'one'      , ''    ),
        (   2, 'two'      , ''    ),
        (   3, 'three'    , ''    ),
        (   4, 'four'     , ''    ),
        (   5, 'five'     , ''    ),
        (   6, 'six'      , ''    ),
        (   7, 'seven'    , ''    ),
        (   8, 'eight'    , ''    ),
        (   9, 'nine'     , ''    ),
        (  10, 'ten'      , ''    ),
        (  11, 'eleven'   , ''    ),
        (  12, 'twelve'   , ''    ),
        (  13, 'thirteen' , ''    ),
        (  14, 'fourteen' , ''    ),
        (  15, 'fifteen'  , ''    ),
        (  16, 'sixteen'  , ''    ),
        (  17, 'seventeen', ''    ),
        (  18, 'eighteen' , ''    ),
        (  19, 'nineteen' , ''    ),
        (  20, 'twenty'   , ''    ),
        (  30, 'thirty'   , ''    ),
        (  40, 'forty'    , ''    ),
        (  50, 'fifty'    , ''    ),
        (  60, 'sixty'    , ''    ),
        (  70, 'seventy'  , ''    ),
        (  80, 'eighty'   , ''    ),
        (  90, 'ninety'   , ''    ),
        ( 100, 'hundred'  , 'and' ),
        (1000, 'thousand' , 'and' )
    ]

    num_to_str.reverse()

    start_time = time.time()
    counter = 0

    for n in range(1, 1001):
        for word in spell(n, num_to_str):
            counter += len(word)
    
    stop_time = time.time()

    print "Runtime: " + str(stop_time - start_time)
    print "Number of letters: " + str(counter)

if __name__ == '__main__':
    main()