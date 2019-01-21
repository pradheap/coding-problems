
def transpose_matrix(matrix):
    ret = []
    if len(matrix) == 0:
        return ret

    first_row = matrix[0]
    for i in range(len(first_row)):
        new_row = []
        for y in range(len(matrix)):
            new_row.append(matrix[y][i])
        ret.append(new_row)
    
    return ret

