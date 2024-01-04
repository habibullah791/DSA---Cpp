def firstDuplicateValue(array):
    map = {}

    idx = 0
    while idx < len(array):
        if array[idx] in map:
            return array[idx]
        else:
            map[array[idx]] = 1
        idx += 1

    return -1


print(firstDuplicateValue([2, 1, 5, 3, 3, 2, 4]))
