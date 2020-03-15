def leonardo_number(n):
    if n == 1 or n == 2:
        return 1
    num1 = num2 = 1
    i = 2
    while i < n:
        l_num = num1 + num2 + 1
        num1 = num2
        num2 = l_num
        i += 1
    return l_num


for i in range(1,101):
    print(leonardo_number(i), end=" ")