#!/usr/bin/env python

def main():
    numbers = []
    max_product = 0

    with open('problem10_input.txt') as f:
        for line in f.readlines():
            line_numbers = line.strip().split(' ')
            numbers.append(map(lambda x: int(x), line_numbers))

    for i in range(20):
        for j in range(16):
            prod = numbers[j][i] * numbers[j+1][i] * numbers[j+2][i] * numbers[j+3][i]
            if prod > max_product: max_product = prod
            prod = numbers[i][j] * numbers[i][j+1] * numbers[i][j+2] * numbers[i][j+3]
            if prod > max_product: max_product = prod
 
    for i in range(16):
        for j in range(16):
            prod = numbers[i][j] * numbers[i+1][j+1] * numbers[i+2][j+2] * numbers[i+3][j+3]
            if prod > max_product: max_product = prod
    for i in range(3,20):
        for j in range(16):
            prod = numbers[i][j] * numbers[i-1][j+1] * numbers[i-2][j+2] * numbers[i-3][j+3]
            if prod > max_product: max_product = prod

    print max_product


if __name__ == '__main__':
    main()