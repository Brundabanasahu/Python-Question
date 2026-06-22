n = int(input())

arr = list(map(int, input().split()))

total_rate = 0

for x in arr:
    total_rate += 1 / x

time = 1 / total_rate

print(f"{time:.2f}")