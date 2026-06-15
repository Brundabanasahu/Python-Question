n1 = int(input())
n2 = int(input())

count = 0

for i in range(n1, n2 + 1):
    num = i
    visited = [False] * 10
    unique = True

    while num > 0:
        digit = num % 10

        if visited[digit]:
            unique = False
            break

        visited[digit] = True
        num //= 10

    if unique:
        count += 1

print(count)