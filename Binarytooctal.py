binary = input("Enter a binary number: ")

decimal = int(binary, 2)
octal_num = oct(decimal)[2:]

print("Octal =", octal_num)