arr=[35,15,45,25,55]
count=0
for i in range(len(arr)):
    if arr[i-1]>arr[i] and arr[i+1]>arr[i]:
        count+=1
print(count)
