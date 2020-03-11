def leonardo_number(n):
    if n == 0 or n == 1:
        return 1
    else:
        return leonardo_number(n-1) + leonardo_number(n-2) + 1


for i in range(10):
    print(leonardo_number(i), end=" ")