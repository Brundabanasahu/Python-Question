n = int(input())
w = list(map(int, input().split()))
Y = int(input())

w.sort()

count = 0
total = 0

for i in range(n):
    if total + w[i] <= Y:
        total += w[i]
        count += 1
    else:
        break

print(count)