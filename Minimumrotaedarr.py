n = int(input("enter the size of the array:"))
arr = list(map(int, input("enter the elements:").split()))

arr.sort()

low=0
high=n-1

while low<high:
    mid=(low+high)//2

    if arr[mid]>arr[high]:
        low=mid+1
    else:
        high=mid

print("minimum element:",arr[low])





# Aggresive cows

#86
#