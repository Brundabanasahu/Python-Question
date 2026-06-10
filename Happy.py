def happy(num):
    seen=set()
    while num!=1 and num not in seen:
        seen.add(num)

        total=0
        while num>0:
            digit=num%10
            total+=digit**2
            num=num//10
        num=total 
    return num==1       

num=int(input())
print(happy(num))