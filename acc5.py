def food(rat,unit,arr):
    if len(arr)==0:
        return -1

    food=rat*unit
    summ=0
    
    for i in range(len(arr)):
        summ+=arr[i]
        if summ>=food:
            return i+1
    return 0    
           


rat = int(input("Enter number of rats: "))
unit = int(input("Enter food per rat: "))
arr = list(map(int, input("Enter food in houses: ").split()))

print(food(rat, unit, arr))