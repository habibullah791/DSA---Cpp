from typing import List, Tuple

def threeSum(array: List[int], targetSum: int) -> List[List[int]]:
    """

    @params:
            array (List[int]): A list of integers.
            targetSum (int): The target sum that the triplets should add up to.

    @desc:  Find all unique triplets in the given list that sum up to the target sum.
    @returns:
            List[List[int]]: A list of unique triplets that sum up to the target sum.
    """
    array.sort()
    ansList = []
    
    for i in range(len(array)):
        left = i + 1
        right = len(array) - 1

        while left < right:
            currentSum = array[left] + array[right] + array[i]
            if currentSum == targetSum:
                temp = [array[i], array[left], array[right]]
                ansList.append(temp)
                left += 1
                right -= 1

            if currentSum < targetSum:
                left += 1

            if currentSum > targetSum:
                right -= 1
    return ansList

if __name__ == "__main__":
    print(threeSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
