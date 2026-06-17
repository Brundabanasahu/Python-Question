n=input()
odd=0
even=0
for i in range(len(n)):
    digit=int(n[i])
    if(i+1)%2==1:
        odd+=digit
    else:
        even+=digit
print(abs(even-odd))       