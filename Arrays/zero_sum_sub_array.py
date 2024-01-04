def zeroSumSubarray(nums):
    sums = set([0])
    currentSum = 0

    for num in nums:
        currentSum = currentSum + num

        if currentSum in sums:
            return True
        else:
            sums.add(currentSum)
    return False


print(zeroSumSubarray([1, 2, -5, 1, 2, -1]))