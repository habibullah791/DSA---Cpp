def transposeMatrix(matrix):
    transposeMatrix = []

    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        transposeMatrix.append(newRow)

    return transposeMatrix


print(transposeMatrix([[1, 2], [3, 4], [5, 6]]))
