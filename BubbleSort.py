def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        didswap=0
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didswap=1
        if didswap==0:
            break        

    return arr            





n = int(input("Enter the size of the array:"))
arr = list(map(int, input("Enter the elements:").split()))        


bubble_sort(arr)

print("Sorted array:")
for i in arr:
    print(i, end=" ") 