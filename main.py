n = int(input("Введите число в восьмеричнной системе счисления (5 разрядов): "))
iflen(n) == 5 and all(char in '01234567' for char in n)
result = 0
for i in range(5):
result += int(n[0]) * (8 ** 4)
result += int(n[1]) * (8 ** 3)
result += int(n[2]) * (8 ** 2)
result += int(n[3]) * (8 ** 1)
result += int(n[4]) * (8 ** 0)
print(result)
