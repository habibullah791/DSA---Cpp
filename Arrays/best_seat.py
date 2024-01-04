def bestSeat(seats):
    bestSeat = -1
    maxSpace = 0

    leftIdx = 0
    rightIdx = leftIdx + 1

    while rightIdx < len(seats):
        if seats[leftIdx] != 0 and seats[rightIdx] != 0:
            space = rightIdx - leftIdx - 1
            seat = (leftIdx + rightIdx) // 2

            if space > maxSpace:
                maxSpace = space
                bestSeat = seat

            leftIdx = rightIdx
        rightIdx += 1

    return bestSeat


print(bestSeat([1, 0, 0, 1, 0, 1]))
