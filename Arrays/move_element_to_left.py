def moveElementToEnd(array, toMove):
    left = 0
    right = 1

    while right < len(array) and left < len(array):
        if array[left] == toMove and array[right] != toMove:
            array[left], array[right] = array[right], array[left]

            left += 1
            if array[right] != toMove:
                right += 1

        if array[left] == toMove and array[right] == toMove:
            right += 1

    return array


print(moveElementToEnd([5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12], 5))
