n = int(input())

arr=list(map(int,input().split()))

result = []
zero = []

for i in arr:
    if i == 0:
        zero.append(0)
    else:
        result.append(i)

result.extend(zero)

print(*result)