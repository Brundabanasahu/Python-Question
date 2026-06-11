b,k,d=map(int,input().split())
key=list(map(int,input().split()))
drive=list(map(int,input().split()))
out=[]
for x in key:
    for y in drive:
        if x+y<=b:
            out.append(x+y)

if not out:
    print(-1)
else:
    print(max(out))                