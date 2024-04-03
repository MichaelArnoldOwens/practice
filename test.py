def findMinDifference(array):
    minDiff = float('inf')

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            # print(array[i] - array[j])
            minDiff = min(minDiff, abs(array[i] - array[j]))
    return minDiff

# print(findMinDifference([1,2,3,4,5,6,7]))
print(findMinDifference([10,2,5]))