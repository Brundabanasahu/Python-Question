def frequency(arr,x,n):
    count=0
    for i in range(n):
        if x==arr[i]:
            count+=1
    return count        






















n = int(input("Enter the size of the array:"))
arr = list(map(int, input("Enter the elements:").split()))
x=int(input("Enter the value of x:"))
print(frequency(arr,x,n))