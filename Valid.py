s=input()
star=0
hash=0
for i in s:
    if i=='*':
        star+=1
    else:
        hash+=1

print(star-hash)