def oddeven(num):
    oddsum=0
    evensum=0
    for i in range(len(num)):
        if i%2==0:
            oddsum+=int(num[i])
        else:
            evensum+=int(num[i])
    return evensum-oddsum
num=input()
print(oddeven(num))