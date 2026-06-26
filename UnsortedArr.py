n=int(input())
arr=list(map(int,input().split()))

currsum=arr[0]
maxsum=0

for i in range(1,len(arr)):
    if arr[i]>arr[i-1]:
        currsum+=arr[i]
    else:
        if currsum>maxsum:
            maxsum=currsum
        currsum=arr[i]
if currsum>maxsum:
    maxsum=currsum

print(maxsum)                    