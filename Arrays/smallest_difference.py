def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    pointerToOne = 0
    pointerToTwo = 0

    smallestDifference = float("inf")
    smallesPair = []
    
    
    while pointerToOne < len(arrayOne) and pointerToTwo < len(arrayTwo):
        diff = abs(arrayOne[pointerToOne] - arrayTwo[pointerToTwo])

        if diff < smallestDifference:
            smallestDifference = diff
            smallesPair = [arrayOne[pointerToOne], arrayTwo[pointerToTwo]]
        if arrayOne[pointerToOne] < arrayTwo[pointerToTwo]:
            pointerToOne += 1
        elif arrayOne[pointerToOne] > arrayTwo[pointerToTwo]:
            pointerToTwo += 1
        else:
            return [arrayOne[pointerToOne], arrayTwo[pointerToTwo]]
    return smallesPair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
