s = input().upper()

one_enclosed = ['A', 'D', 'O', 'P', 'Q', 'R']
two_enclosed= ['B']

count = 0

for ch in s:
    if ch in one_enclosed:
        count += 1
    elif ch in two_enclosed:
        count += 2

print(count)