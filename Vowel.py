def vow(s):
    vowel=0
    con=0
    for ch in s.lower():
        if ch in "aeiou":
            vowel+=1
        elif ch>='a' and ch<='z':
            con+=1

    return vowel,con

s=input()
v,c=vow(s)
print("Vowels =", v)
print("Consonants =", c)

 
# 29
# 34