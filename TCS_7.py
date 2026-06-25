n=int(input())
arr = list(map(int, input().split()))
evencount=0
oddcount=0

for i in range(len(arr)):
    if arr[i]%2==0:
        evencount+=1
    else:         
        oddcount+=1

if evencount==oddcount:
    print(n)
else:
    print("0")          