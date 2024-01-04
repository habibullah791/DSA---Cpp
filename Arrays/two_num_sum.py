def twoNumberSum(array, targetSum):
    map = {}

    for idx in array:
        target = targetSum - idx

        if target in map:
            return [idx, target]
        else:
            map[idx] = True

    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
