n = int(input())
arr = list(map(int, input().split()))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for key in sorted(freq):
    print(key, freq[key])