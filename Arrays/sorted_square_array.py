def sortedSquaredArray(array):
    # create array of size array
    newArray = [0 for _ in array]

    # -3, -2, -1

    LEFT = 0
    RIGHT = len(array) - 1

    for idx in reversed(range(len(array))):
        smallestValue = array[LEFT]
        greatestValue = array[RIGHT]

        if abs(smallestValue) > abs(greatestValue):
            newArray[idx] = smallestValue * smallestValue
            LEFT += 1
        else:
            newArray[idx] = greatestValue * greatestValue
            RIGHT -= 1

    return newArray


print(sortedSquaredArray([-3, -2, -1]))
