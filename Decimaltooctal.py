def decimal(n1):
    if n1==0:
        return "0"
    
    octal=""
    while n1>0:
        octal=str(n1%8)+octal
        n1=n1//8
    return octal


n1=int(input())
print(decimal(n1))