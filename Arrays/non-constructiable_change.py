def nonConstructibleChange(coins):
    # Write your code here.

    coins.sort()
    change = 0
    i = 0
    
    while i < len(coins):
        if coins[i] > change + 1:
            return change + 1
        else:
            change += coins[i]
            i += 1
    return change + 1


# print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))
print(nonConstructibleChange([1, 2, 3, 4, 5, 6, 7]))
