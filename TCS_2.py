s1=input()
result=""
for i in range(len(s1)):
    ch=s1[i]
    if i%2==0:
        if ch=='Z':
            result+='B'
        elif ch=='Y':
            result+='A'
        elif ch=='z':
            result+='b'
        elif ch=='y':
            result+='b'
        else:
            result+=  chr(ord(ch)+2)
     # Odd index: -1
    else:
        if ch == 'A':
            result += 'Z'
        elif ch == 'a':
           result += 'z'
        else:
            result += chr(ord(ch) - 1)                  


print(result)

#partiaally correct
# s1=input()
# result=""
# for i in range(len(s1)):
#     ch=s1[i]
#     if i%2==0:
#         result+=chr(ord(ch)+2)
#     else:
#         result+=chr(ord(ch)-1)
# print(result)            