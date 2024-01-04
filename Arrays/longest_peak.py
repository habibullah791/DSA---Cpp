def longestPeak(array):
    # Write your code here.
    # [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

    longestPeakLenght = 0
    idx = 1

    while idx < len(array) - 1:
        isPeak = array[idx - 1] < array[idx] and array[idx] > array[idx + 1]

        if not isPeak:
            idx += 1
            continue

        leftIdx = idx - 2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1

        rightIdx = idx + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        currentPeakLenght = rightIdx - leftIdx - 1
        longestPeakLenght = max(currentPeakLenght, longestPeakLenght)

        idx = rightIdx

    return longestPeakLenght


print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
# longestPeak([1, 3, 2])  # 3
