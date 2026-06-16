n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements: ").split()))
destination=int(input("Enter the number you want to search"))
found=False

for i in range(n):
    if arr[i]==destination:
           found=True
           break

if found:
      print("Element found")
else:
      print("Element not found")          