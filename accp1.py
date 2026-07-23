m=int(input())
n=int(input())
div=0
notdiv=0
for i in range(1,n+1):
    if i%m==0:
        div+=i
    else:
        notdiv+=i

print(notdiv-div)

