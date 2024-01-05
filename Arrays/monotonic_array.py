def isMonotonic(array):
    # Write your code here.
    isNonIncreasing = True
    isNonDecreasing = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
        if array[i] > array[i - 1]:
            isNonIncreasing = False

    return isNonIncreasing or isNonDecreasing
    

print(isMonotonic([1, 2, 3, 4, 5, 0]))
