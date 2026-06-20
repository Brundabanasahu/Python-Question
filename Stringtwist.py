s1 = input()
s2 = input()
s3 = input()

vowel = "aeiouAEIOU"
result = ""


for i in s1:
    if i in vowel:
        result+="%"
    else:
        result+=i


for i in s2:
    if i not in vowel:
        result+="#"
    else:
        result+=i


for ch in s3:
    if 'a'<=ch<='z':
        result+=chr(ord(ch)-32)
    else:
        result+=ch

print(result)