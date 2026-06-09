def digit(n1):
    string=str(n1)
    count=0
    for i in string:
        digit=int(i)
        if digit!=0 and n1%digit==0:
            count+=1
    return count        




n1=int(input())
print(digit(n1))