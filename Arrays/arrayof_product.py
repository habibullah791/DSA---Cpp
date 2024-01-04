def arrayOfProducts(array):
    # Write your code here.
    result = []

    idx = 0

    while idx < len(array):
        leftIdx = idx - 1
        rightIdx = idx + 1

        leftProd = 1
        rightProd = 1

        while leftIdx >= 0:
            leftProd *= array[leftIdx]
            leftIdx -= 1

        while rightIdx < len(array):
            rightProd *= array[rightIdx]
            rightIdx += 1

        print(leftProd)
        print(rightProd)

        currentProd = leftProd * rightProd
        result.append(currentProd)

        idx += 1
        # break

    return result


print(arrayOfProducts([5, 1, 4, 2]))
