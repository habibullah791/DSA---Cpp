def majorityElement(array):
    # Write your code here.
    count = 0
    answer = None

    for num in array:
        if count == 0:
            answer = num
        if answer == num:
            count += 1
        else:
            count -= 1

    return answer


majorityElement([1, 2, 3, 2, 2, 1, 2])
