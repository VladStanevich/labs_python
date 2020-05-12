def leonardo_number(n):
    try:
        if n <= 0 or type(n) is not int:
            print("Вы ввели не натуральное число")
        elif n == 1 or n == 2:
            return 1
        else:
            num1 = num2 = 1
            i = 2
            while i < n:
                num1, num2 = num2, num1 + num2 + 1 
                i += 1
            return num2
    except ValueError:
        print("Вы ввели не число")


if __name__ == "__main__":
    print(leonardo_number(-100))


