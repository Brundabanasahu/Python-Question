n = int(input())
arr = list(map(int, input().split()))

neg = []
product = 1
zero = 0

for x in arr:
    if x == 0:
        zero += 1
    else:
        product *= x

    if x < 0:
        neg.append(x)

# All zeros
if zero == n:
    print(0)

# Odd number of negatives
elif len(neg) % 2 == 1:
    mx = max(neg)      # negative closest to 0
    print(product // mx)

else:
    print(product)