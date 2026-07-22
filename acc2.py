n=int(input("Enter the size of the array:"))
arr=list(map(int,input("Enter the elements of the array:").split()))
summ=int(input("Enter the sum:"))

if n<2:
    print(-1)
    exit()

firstsmallest=float('inf')
secondsmallest=float('inf')
for i in range(0,n):
    if arr[i]<firstsmallest:
        secondsmallest=firstsmallest
        firstsmallest=arr[i]
    elif arr[i]<secondsmallest and arr[i]!=firstsmallest:
        secondsmallest=arr[i]    

if (firstsmallest+secondsmallest)<=summ:
    print(firstsmallest*secondsmallest)
else:
    print(0)


