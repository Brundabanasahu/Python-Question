s1=input()
first=s1[0]
last=0
count=0
for i in range(len(s1)):
    if s1[i]==first:
        last=i
for i in range(1,last):
    count+=1

print(count)        
        