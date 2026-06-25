try:
    n = int(input())

    if n < 0:
        print("error")

    elif n <= 2:
        print(n * 100)

    elif n <= 5:
        print(2 * 100 + (n - 2) * 50)

    else:
        print(2 * 100 + 3 * 50 + (n - 5) * 20)

except:
    print("error")