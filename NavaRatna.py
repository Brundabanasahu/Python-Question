n=int(input())
x=0
y=0

for i in range(1,n+1):
    distance=i*10
    
    if i%4==1:
        x+=distance
    elif i%4==2:
        y+=distance
    elif i%4==3:
        x-=distance
    else:
        y-=distance

print(x,y)