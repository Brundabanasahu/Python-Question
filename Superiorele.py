n=int(input("Enter the size of the array:"))



if n==0:
    print("0")
    
else:
    arr=list(map(int,input("Enter the elements of the array:").split()))
    count=1
    maxi=arr[n-1]

    i=n-2
    while i>=0:
        if arr[i]>maxi:
            count+=1
            maxi=arr[i]
        i-=1

    print(count)