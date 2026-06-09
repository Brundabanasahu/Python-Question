def gcd(n1,n2):
    while n2:
        a,b=b,a%b
    return a    

n1=int(input())
n2=int(input())
n3=int(input())
print(gcd(gcd(n1,n2),n3))