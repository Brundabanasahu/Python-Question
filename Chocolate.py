greed=[2,1,2,5,4,3]
choco=[1,2,1,3,2,3,4]
greed.sort()
choco.sort()
left=0
right=0
while left<len(greed)and right<len(choco):
    if choco[right]>=greed[left]:
        left+=1
    right+=1  

print(left) 