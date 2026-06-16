n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements: ").split()))
target = int(input("Enter the number you want to search: "))

arr.sort()

first = -1
last = -1

# Search for first occurrence
low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid]==target:
        first=mid
        high=mid-1
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1

# Search for last occurrence
low=0
high=n-1

while low<=high:
    mid =(low + high)//2

    if arr[mid]==target:
        last=mid
        low=mid+1
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1

if first == -1:
    print("Element not found")
else:
    print("First position:", first)
    print("Last position:", last)