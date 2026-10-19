#!/usr/bin/env python3


def rotate_matrix(matrix):
    """Rotate a square matrix 90 degrees counter-clockwise, in place.

    A cell (row, col) is encoded as the complex number row + col*j.
    Multiplying by j rotates it 90 degrees about the origin to (-col, row),
    and adding N-1 shifts it back into range: (row, col) -> (N-1-col, row).

    Every cell except the center of an odd-sized matrix belongs to a cycle
    of 4 cells that map onto each other. Each cycle is rotated by walking it
    once and shifting the values along.

    O(N^2) time, O(1) extra space.
    """
    N = len(matrix)
    # One starting cell per 4-cycle: a ceil(N/2) x floor(N/2) quadrant.
    # For odd N, the center cell maps to itself and is skipped.
    for i in range((N+1)//2):
        for j in range((N)//2):
            coor = complex(i, j)
            val = matrix[i][j]

            # Walk the cycle: put the carried value into the next cell and
            # pick up that cell's old value. After 4 steps we are back at
            # (i, j), which receives the value of the last cell.
            for _ in range(4):
                # Rotate by 90 degrees about the origin, then shift into range.
                coor = coor * complex(0, 1) + complex(N-1, 0)
                x = int(coor.real)
                y = int(coor.imag)
                val, matrix[x][y] = matrix[x][y], val


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(f'{col} ', end='')
        print('')


if __name__ == '__main__':
    tests = (
        ([], []),                                       # empty matrix: nothing to rotate
        ([[1]], [[1]]),                                 # 1x1: the single cell is the center
        ([[1,2], [3,4]], [[2,4], [1,3]]),               # 2x2: a single 4-cycle
        ([[1,2,3], [4,5,6], [7,8,9]],                   # odd N: the center stays put
         [[3,6,9], [2,5,8], [1,4,7]]),
        ([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]],      # even N: two layers
         [[4,8,12,16], [3,7,11,15], [2,6,10,14], [1,5,9,13]]),
        ([[1,2,3,3], [4,5,6,6], [7,8,9,9], [0,0,0,9]],  # duplicate values
         [[3,6,9,9], [3,6,9,0], [2,5,8,0], [1,4,7,0]]),
        ([[7,7,7], [7,7,7], [7,7,7]], [[7,7,7], [7,7,7], [7,7,7]]),  # all equal: unchanged
        ([[-1,0], [0,1]], [[0,1], [-1,0]]),             # negative values
        ([[r*5 + c for c in range(5)] for r in range(5)],          # 5x5: two layers plus a center
         [[4,9,14,19,24], [3,8,13,18,23], [2,7,12,17,22], [1,6,11,16,21], [0,5,10,15,20]]),
    )

    for test in tests:
        matrix = [row[:] for row in test[0]]    # rotation is in place, so work on a copy
        rotate_matrix(matrix)
        assert matrix == test[1], f'Expected {test[1]}, got {matrix} instead'

        # four quarter turns must give back the original matrix
        for _ in range(3):
            rotate_matrix(matrix)
        assert matrix == test[0], f'Expected {test[0]} after a full turn, got {matrix} instead'
    print('All tests PASSED')

