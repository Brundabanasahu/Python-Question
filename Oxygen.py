oxygen = []

for i in range(9):
    n = int(input())

    if n < 1 or n > 100:
        print("INVALID INPUT")
        exit()

    oxygen.append(n)

t1 = round((oxygen[0] + oxygen[3] + oxygen[6]) / 3)
t2 = round((oxygen[1] + oxygen[4] + oxygen[7]) / 3)
t3 = round((oxygen[2] + oxygen[5] + oxygen[8]) / 3)

maximum = max(t1, t2, t3)

if maximum < 70:
    print("All trainees are unfit.")
else:
    if t1 == maximum:
        print("Trainee Number :", 1)

    if t2 == maximum:
        print("Trainee Number :", 2)

    if t3 == maximum:
        print("Trainee Number :", 3)