data = list(map(int, input().split()))

n = data[0]
arr = data[1:]

if len(arr) != n:
    print("Wrong Input")
else:
    arr.sort()

    for i in range(1, n):
        if arr[i] <= arr[i - 1]:
            arr[i] = arr[i - 1] + 1

    print(sum(arr))