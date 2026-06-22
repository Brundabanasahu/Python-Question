n=int(input())
x=n+1
while True:
    root=int(x**0.5)
    if root*root==x:
        print(x)
        break
    x+=1