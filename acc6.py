def operationBinaryString(s):

    if s is None or len(s) == 0:
        return -1

    result = int(s[0])

    i = 1
    while i < len(s):
        op = s[i]
        num = int(s[i + 1])

        if op == 'A':
            result = result & num
        elif op == 'B':
            result = result | num
        elif op == 'C':
            result = result ^ num

        i += 2

    return result


# Driver Code
s = input("Enter binary string: ")
print(operationBinaryString(s))