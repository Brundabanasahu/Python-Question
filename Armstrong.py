def Arm(n1):
    total=0
    length=len(str(n1))
    temp=n1
    while n1>0:
        last=n1%10
        total+=last**length
        n1=n1//10
    return total==temp
    
        
n1=int(input())
if Arm(n1):
    print("Armstrong")
else:
    print("Not Armstrong")        