# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

# Example 1:

# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]

def flip_image(matrix):
    for row in matrix:
        first = 0
        last = len(row) - 1
        while first < last:
            row[first], row[last] = row[last], row[first]
            first += 1
            last -= 1
        for i in range(len(row)):
            row[i] ^= 1

    return matrix
