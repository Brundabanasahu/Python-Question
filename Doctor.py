total=0
for i in range(20):
    age=input()

    if age=="":
        break

    age=int(age)


    if age<=0 or age>120:
        print("Invalid input")
        exit()



    if age<17:
        total+=200
    elif age<=40:
        total+=400
    else:
        total+=300


print(total)