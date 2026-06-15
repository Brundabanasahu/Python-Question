def rotate(arr, n, k):
    k = k % n
    result = []

    
    for i in range(n - k, n):
        result.append(arr[i])

    
    for i in range(n - k):
        result.append(arr[i])

    return result


n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements: ").split()))
k = int(input("Enter the value of K: "))

print(rotate(arr, n, k))