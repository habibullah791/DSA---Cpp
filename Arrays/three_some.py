def threeNumberSum(array, targetSum):
    array.sort()

    triplets = []

    i = 0
    while i < len(array):
        current = array[i]

        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = current + array[left] + array[right]

            if currentSum < targetSum:
                left += 1
            if currentSum > targetSum:
                right -= 1
            if currentSum == targetSum:
                triplets.append([current, array[left], array[right]])
                left += 1
                right -= 1
        i += 1
    return triplets


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
