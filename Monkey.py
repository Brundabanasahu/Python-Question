n = int(input())
k = int(input())
j = int(input())
m = int(input())
p = int(input())

if n < 0 or k <= 0 or j <= 0 or m < 0 or p < 0:
    print("INVALID INPUT")
else:
    monkeys = (m // k) + (p // j)

    if m % k != 0 or p % j != 0:
        monkeys += 1

    left = n - monkeys

    if left < 0:
        left = 0

    print("Number of Monkeys left on the tree:", left)