def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j

        arr[mini],arr[i]=arr[i],arr[mini]

    return arr


n = int(input("Enter the size of the array:"))
arr = list(map(int, input("Enter the elements:").split()))

selection_sort(arr)

print("Sorted array:")
for i in arr:
    print(i, end=" ")