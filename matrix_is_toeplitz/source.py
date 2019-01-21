# A matrix is Toeplitz if every diagonal from top-left to bottom-right has 
# the same element.
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

# Input:
# matrix = [
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]
# Output: True

def is_toeplitz(matrix):
    rows = len(matrix)
    if rows == 0:
        return False
    cols = len(matrix[0])
    if cols == 0:
        return False

    # Diagonal check starts from the first row first element and don't care 
    # about the last element.
    for col in range(cols - 1):
        first_row = 0
        start = matrix[first_row][col]
        diagonal = col
        curr_row = first_row + 1
        while curr_row < rows and diagonal < cols - 1:
            diagonal += 1
            if start != matrix[curr_row][diagonal]:
                return False
            curr_row += 1

    # Diagonal check starts from the second element in the first column and 
    # doesn't care about the last element.
    for row in range(1, rows - 1):
        first_col = 0
        start = matrix[row][first_col]
        diagonal = first_col
        curr_row = row + 1
        while curr_row < rows and diagonal < cols - 1:
            diagonal += 1
            if start != matrix[curr_row][diagonal]:
                return False
            curr_row += 1
        
    return True

# Concise solution once you realize each row is offset of the previous 
# row with a new element on the left and the last element truncated.
def is_toeplitz_v1(matrix):
    rows = len(matrix)
    if rows == 0:
        return False
    cols = len(matrix[0])
    if cols == 0:
        return False
    
    prev = matrix[0]
    for i in range(1, rows):
        for j in range(cols - 1):
            if prev[j] != matrix[i][j + 1]:
                return False
        prev = matrix[i]
    
    return True


