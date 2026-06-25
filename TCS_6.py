n = int(input())
arr = list(map(int, input().split()))

freq = [0] * (n + 1)

for num in arr:
    freq[num] += 1

dupli = -1
miss = -1

for i in range(1, n + 1):
    if freq[i] == 2:
        dupli = i

    if freq[i] == 0:
        miss = i

print(dupli, miss)