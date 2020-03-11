def dvoechka(n):
    while(n != 1):
        if n % 2 == 0:
            n = n // 2 
        else:
            return False
    return True

print(dvoechka(256))