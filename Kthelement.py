n = int(input("Enter the size of the array:"))
arr = list(map(int, input("Enter the elements:").split())) 
k=int(input("enter the kth element"))

for i in range(k):
    mini= i
    for j in range(i + 1, n):
        if arr[j] < arr[mini]:
            mini = j

    arr[i], arr[mini] = arr[mini], arr[i]

print("Kth smallest element is:", arr[k - 1])