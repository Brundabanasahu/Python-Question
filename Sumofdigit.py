def digit(num):
    while num>9:
        total=0
        while num>0:
            digit=num%10
            total+=digit
            num=num//10
        num=total
    return num        
    

num=int(input())
print(digit(num))    
if digit(num)==1:
    print("UNO")
else:
    print("NOT UNO")    