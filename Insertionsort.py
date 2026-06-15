def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
            

    return arr        

n = int(input("Enter the size of the array:"))
arr = list(map(int, input("Enter the elements:").split()))  



insertion_sort(arr)

print("Sorted array:")
for i in arr:
    print(i, end=" ") 