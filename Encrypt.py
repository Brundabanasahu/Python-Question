def caesar(s,key):
    result = ""

    for ch in s:
        if 'a'<=ch<='z':
            result+=chr((ord(ch)-ord('a')+key)%26+ord('a'))
        elif 'A'<=ch<='Z':
            result+=chr((ord(ch)-ord('A')+key)%26+ord('A'))    
        elif '0'<=ch<='9':
            result+=str((int(ch)+key)%10)
        else:
            result+=ch
    return result


s=input()
key=int(input())
print(caesar(s, key))

# insertion
# merge

