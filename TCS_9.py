n = int(input())

seen = {}

for i in range(n):
    sender, receiver, amount, time = input().split()

    amount = int(amount)
    time = int(time)

    key = (sender, receiver, amount)

    if key in seen:
        prev_time = seen[key]

        if time - prev_time <= 60:
            print("Fraud transaction")

    seen[key] = time