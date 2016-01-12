#!/usr/bin/env python

def main():
    numbers = []

    with open('problem13_input.txt') as f:
        for line in f.readlines():
            numbers.append(long(line.strip()))

    longsum = sum(numbers)
    strsum = str(longsum)
    print strsum[0:10]


if __name__ == '__main__':
    main()