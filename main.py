n = int(input("Введите число в восьмеричнной системе счисления (5 разрядов): "))
eight_last = n % 10
n //=10
ten_last = eight_last * (8 ** 0)
eight_fourth = n % 10
n //= 10
ten_fourth = eight_fourth * (8 ** 1)
eight_ten = n % 10
n //= 10
ten_third = e_t * (8 ** 2)
eight_second = n % 10
n //= 10
ten_second = eight_second * (8 ** 3)
eight_first = n % 10
n //= 10
ten_first = eight_first * (8 ** 4)
sum = ten_last + ten_fourth + ten_third + ten_second + ten_first
print(f"Число {n} в восьмеричной системе счисления =  число {sum} в десятичной системе счисления")
