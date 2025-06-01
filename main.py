import math


while True:
    try:
        n = int(input("Введите число от 1 до 999: "))
        if n < 0:
            print("Вы ввели отрицательное число!")
        elif n > 999:
            print("Вы ввели число больше 999!")
        else:
            result = math.factorial(n)
            print("Факториал числа ", n, "равен ", result)
            break
    except ValueError:
        print("Вы ввели не число!")


