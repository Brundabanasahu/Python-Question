n=int(input())
count=0
temp=abs(n)
for i in str(temp):
    digit=int(i)
    if digit !=0 and temp%digit==0:
        count+=1
print(count)        
