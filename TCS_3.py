def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True    

n=int(input())
s=int(input())

count=0
num=s
nthprime=0

while count<n:
    if isprime(n):
        count+=1
        
        if count==n:
           nthprime=num
           break 
    num+=1 


total=nthprime
found=0
nextnum=nthprime+1

while found<2:
    if isprime(nextnum):
        total+=nextnum
        found+=1
    nextnum+=1    

print(total)