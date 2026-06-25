n = int(input())

if n == 3:
    print(5000)

elif n == 6:
    print(7000)

elif n == 9:
    print(12000)

elif n == 12:
    print(15000)

elif n == 15:
    print(20000)   # 12 + 3

elif n == 18:
    print(22000)   # 12 + 6

elif n == 21:
    print(27000)   # 12 + 9

elif n == 24:
    print(30000)   # 12 + 12

else:
    print("Error")



n = int(input())

plans = {
    12: 15000,
    9: 12000,
    6: 7000,
    3: 5000
}

cost = 0

for months in [12, 9, 6, 3]:
    while n >= months:
        n -= months
        cost += plans[months]

if n == 0:
    print(cost)
else:
    print("Error")