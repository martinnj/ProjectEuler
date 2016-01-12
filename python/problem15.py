#!/usr/bin/env python

import time

def recursive_path_counter(grid_size):
    """
    Takes a billion years, but easy to make and see that it is true :)
    """
    paths = 0

    if grid_size == [0,0]:
        return 1
    if grid_size[0] > 0:
        paths += recursive_path_counter([grid_size[0]-1, grid_size[1]])
    if grid_size[1] > 0:
        paths += recursive_path_counter([grid_size[0], grid_size[1]-1])
 
    return paths

def dynamic_programming_path_counter(grid_size):
    """
    Dynamic programming is so nice. Assumes the grid is square though.
    """
    G = [1] * grid_size
    for i in range(grid_size):
        for j in range(i):
            G[j] = G[j] + G[j-1]
        G[i] = 2 * G[i - 1]
    return G[grid_size - 1]

def main():
    start_time = time.time()
    grid_size = [20,20]

    #num_paths = recursive_path_counter(grid_size)
    num_paths = dynamic_programming_path_counter(grid_size[0])
    stop_time = time.time()

    print "Runtime: " + str(stop_time - start_time)
    print "Number of paths: " + str(num_paths)

if __name__ == '__main__':
    main()