def spiralTraverse(array):
    # Write your code here.

    results = []

    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1


array = [
    [19, 32, 33, 34, 25, 8],
    [16, 15, 14, 13, 12, 11],
    [18, 31, 36, 35, 26, 9],
    [1, 2, 3, 4, 5, 6],
    [20, 21, 22, 23, 24, 7],
    [17, 30, 29, 28, 27, 10],
]


print(spiralTraverse(array))
