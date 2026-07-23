def productSmallPair(arr, target):
    arr.sort()

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return arr[i] * arr[j]

    return -1


arr = [5, 2, 4, 3, 9, 7, 1]
target = 5

print(productSmallPair(arr, target))