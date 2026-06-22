s = input().strip().upper()

value = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16
}

decimal = 0
power = len(s) - 1

for ch in s:
    if ch.isdigit():
        digit = int(ch)
    else:
        digit = value[ch]

    decimal += digit * (17 ** power)
    power -= 1

print(decimal)