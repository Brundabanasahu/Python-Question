n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements: ").split()))
destination=int(input("Enter the number you want to search"))

arr.sort()

low=0
high=n-1
found=False

while low<=high:
    mid=(low+high)//2
    if arr[mid]==destination:
        found = True
        break
    elif arr[mid]<destination:
        low =mid+1
    else:
        high=mid-1

if found:
    print("Element found at index", mid)
else:
    print("Element not found")