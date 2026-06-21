s1=input()
key=int(input())
if key<0:
    print("Invalid input")
    exit()
result=""   
for ch in s1:
    if ch.isupper():
          result+=chr((ord(ch)-ord('A')+key)%26+ord('A'))
    elif ch.islower():
          result+=chr((ord(ch)-ord('a')+key)%26+ord('a'))
    elif ch.isdigit():
          result+=str((int(ch)+key)%10)  
    else:
         result+=ch

print(result)                  