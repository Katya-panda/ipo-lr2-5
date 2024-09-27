import math
def octal_to_decimal(octal_number):
    decimal_value = 0
    for index, digit in enumerate(reversed(octal_number)):
        decimal_value += int(digit) * (8 ** index)
        return decimal_value
    def main():
        octal_input = input("Введите число в восьмеричной системе счисления (5 разрядов): ")
        if len(octal_input) != 5 or not all (digit in '01234567' for digit in octal_input):
            print("Ошибка: Введите корректное число в восьмеричной системе счисления из 5 разрядов.")
            return
        decimal_output = octal_to_decimal(octal_input)
        print("Число в десятичной системе счисления: ", decimal_output)
