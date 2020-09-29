# percolation.py

import numpy as np
import sys

# Global variable needed
flag = False

# Functions
def matrix_fill(p, n):
    '''
    Fills square matrix with 0 and 1.
    '''
    return np.random.rand(n, n) < p

def matrix_print(matrix):
    '''
    Prints the matrix on the screen.
    '''
    print(matrix)
    
def matrix_is_passable(n, matrix):
    '''
    Finds out if the given matrix is passable.
    '''
    # Number of elements in the matrix
    n = len(matrix[0])
    # Flag
    global flag
    flag = False

    for i in range(n):
        if flag:
            return True
        matrix_recursive_check(n, matrix, i, 0)

    return False

# Used in function above
def matrix_recursive_check(n, matrix, i, j):
    '''
    Recursively check the path from a given point (i, j).
    '''
    # Flag
    global flag
    # Check if current point is false or the path is already found
    if not matrix[i, j] or flag:
        return

    # Do nothing if reached the end
    if j == n - 1:
        flag = True
        return

    # Prevent function from going back
    matrix[i, j] = False

    # Find path
    if matrix[i, j + 1]:
        matrix_recursive_check(n, matrix, i, j + 1)
    if i != 0 and matrix[i - 1, j]:
        matrix_recursive_check(n, matrix, i - 1, j)
    if i != n - 1 and matrix[i + 1, j]:
        matrix_recursive_check(n, matrix, i + 1, j)
    if j != 0 and matrix[i, j - 1]:
        matrix_recursive_check(n, matrix, i, j - 1)

def matrix_get_probability(n, p, k):
    '''
    Calculates the probability of conductivity of the matrix of a given size.
    '''
    P = 0
    for i in range(k):
        matrix = matrix_fill(p, n)
        # matrix_print(matrix)

        if matrix_is_passable(n, matrix):
            P += 1

    return P / k

def percolation(n, n_experiments, n_attempts):
    '''
    Main function.
    '''
    p, dp = 0, 1 / (n_experiments - 1)
    with open(f'{n}x{n}_{n_experiments}_{n_attempts}.txt', 'w+') as output_file:
        for i in range(n_experiments):
            output_file.write(f'{p} {matrix_get_probability(n, p, n_attempts)}\n') 
            p += dp

if __name__ == '__main__':
    if len(sys.argv) != 4: 
        raise ValueError(f'Expected 3 arguments: <size> <n_experiments> <n_attempts>, got {len(sys.argv) - 1}.')
    else:
        percolation(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
