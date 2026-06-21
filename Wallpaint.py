interior = int(input())
exterior = int(input())

if interior < 0 or exterior < 0:
    print("INVALID INPUT")
else:
    total_cost = 0

    for i in range(interior):
        area = float(input())
        total_cost += area * 18

    for i in range(exterior):
        area = float(input())
        total_cost += area * 12

    print("Total estimated Cost :", total_cost, "INR")