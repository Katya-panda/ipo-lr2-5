n = int(input("Введите число в восьмеричнной системе счисления (5 разрядов): "))
result = 0
result += int(n[0]) * (8 ** 4)
result += int(n[1]) * (8 ** 3)
result += int(n[2]) * (8 ** 2)
result += int(n[3]) * (8 ** 1)
result += int(n[4]) * (8 ** 0)
print(result)
