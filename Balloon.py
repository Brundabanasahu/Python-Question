n = int(input())
arr = input().split()

freq = {}


for color in arr:
    if color in freq:
        freq[color] += 1
    else:
        freq[color] = 1

found = False

for color in arr:
    if freq[color] % 2 != 0:
        print(color)
        found = True
        break

if not found:
    print("All are even")