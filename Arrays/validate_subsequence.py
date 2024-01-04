def isValidSubsequence(array, sequence):
    LEFT = 0
    i = 0


    while LEFT < len(sequence) and i < len(array):
        if array[i] == sequence[LEFT]:
            LEFT += 1
        i += 1

    if LEFT == len(sequence):
        return True
    else:
        return False


print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -2]))
