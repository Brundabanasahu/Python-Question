n = int(input("Enter the size of the array:"))
arr = list(map(int, input("Enter the elements:").split()))


mini= float('inf')

for i in range(n):
    for j in range(i+1,n):
        diff = abs(arr[i]-arr[j])
        if diff<mini:
            mini = diff

print("Minimum difference =", mini)