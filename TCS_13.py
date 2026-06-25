n = int(input())
A = list(map(int, input().split()))

m = int(input())
B = list(map(int, input().split()))

# Reverse B to make it ascending
B = B[::-1]

i = j = 0
result = []

while i < n and j < m:
    if A[i] <= B[j]:
        result.append(A[i])
        i += 1
    else:
        result.append(B[j])
        j += 1

while i < n:
    result.append(A[i])
    i += 1

while j < m:
    result.append(B[j])
    j += 1

print(*result)