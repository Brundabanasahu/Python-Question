N=10
K=5
num=int(input("take number of candies"))

if num>(N-K):
    print("Invalid input")
else:    
    print("Number of candies sold: ",num)
    print("Number of canides available: ",N-num)