import numpy as np

def invert_diagonals(matrix):
    firstDiag = np.array(np.fliplr(matrix.diagonal()))
    secondDiag = np.array(np.fliplr(np.fliplr(matrix).diagonal()))

    np.fill_diagonal(matrix, firstDiag)
    np.fill_diagonal(np.fliplr(matrix), secondDiag)
    return matrix

def matrix_contains(matrixA, matrixB):
    rowA = matrixA[0].size
    columnA = matrixA[:, 0].size

    rowB = matrixB[0].size 
    columnB = matrixB[:, 0].size

    counter = 0

    for row in range(rowA):
        for col in range(columnA):
            # compare the element with the first one in the second matrix #
            # if remainig rows and columns are lower than matrixB it won't calculate #
            if matrixA[col,row] == matrixB[0,0] and row + rowB <= rowA and col + columnB <= columnA:
                # create a new matrix based on the size of matrixB and compare both #
                matrixAux = matrixA[ col:col+columnB, row:row+rowB ]
                if (matrixAux & matrixB).all():
                    counter += 1
                

    return counter
            