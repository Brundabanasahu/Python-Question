n=int(input())
data = list(map(int, input().split()))
arr=[30,60,120]
for i in range(len(data)):
    if data[i]==arr:
        print("Successful")
    else:
        print("failed")    