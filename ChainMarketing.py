amount = 5000

parent = input()
choice = input().upper()

children = []

if choice == 'Y':
    children = input().split(',')

print("TOTAL MEMBERS:", len(children) + 1)
print("COMISSION DETAILS")

if len(children) == 0:
    print(parent + ":", int(amount * 0.05), "INR")
else:
    print(parent + ":", len(children) * int(amount * 0.10), "INR")

for child in children:
    print(child.strip() + ":", int(amount * 0.05), "INR")