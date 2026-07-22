n=int(input("Enter a number:"))
while n>=10:
    if n%2==0:
        n=(n-2)//2
    else:
        n=n//2
print(n)        