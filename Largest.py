s = input()

num = ""
maximum = -1
for ch in s:
    if ch.isdigit():
        num+=ch
    else:
        if num!="":
            if '9' not in num:
                maximum=max(maximum, int(num))
            
if num != "":
    if '9' not in num:
        maximum = max(maximum, int(num))

print(maximum)