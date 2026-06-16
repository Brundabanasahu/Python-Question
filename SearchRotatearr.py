n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements: ").split()))
target = int(input("Enter the number to search: "))

low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element found at index", mid)
        break

    # Left half is sorted
    if arr[low] <= arr[mid]:
        if arr[low] <= target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    # Right half is sorted
    else:
        if arr[mid] < target <= arr[high]:
            low = mid + 1
        else:
            high = mid - 1

else:
    print("Element not found")