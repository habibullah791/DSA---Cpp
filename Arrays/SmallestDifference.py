from typing import List

def smallestDifference(arrayOne: List[int], arrayTwo: List[int]) -> List[int]:
    """
    @desc:      Find the pair of elements, one from each input list, with the smallest absolute difference.
    @param:
                arrayOne (List[int]): The first input list of integers.
                arrayTwo (List[int]): The second input list of integers.
    @returns:
                List[int]: A list containing the pair of elements (one from each input list)
                with the smallest absolute difference.
    """
    arrayOne.sort()
    arrayTwo.sort()
    
    i = 0
    j = 0
    ans = []

    smallest = float("inf")
    
    while i < len(arrayOne) and j < len(arrayTwo):
        diff = abs(arrayOne[i] - arrayTwo[j])

        if diff == 0:
            return [arrayOne[i], arrayTwo[j]]

        elif diff < smallest:
            smallest = diff
            ans = [arrayOne[i], arrayTwo[j]]

        if arrayOne[i] < arrayTwo[j]:
            i += 1

        elif arrayOne[i] > arrayTwo[j]:
            j += 1

    return ans

if __name__ == "__main__":
    print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
