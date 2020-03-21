import math


def sqrt_decomposition(A: list, l, r):
    l = l-1
    r = r-1 
    number_box = math.ceil(math.sqrt(len(A)))
    length_box = math.ceil(len(A) / number_box)
    B = [0]*number_box
    for i in range(len(A)):
        B[i // length_box] += A[i]
    summa = 0
    l_box = l // length_box
    r_box = r // length_box
    if l_box == r_box:
        for i in range(l, r+1):
            summa += A[i]
    else:
        for i in range(l, (l_box+1)*length_box):
            summa += A[i]
        for i in range(l_box+1, r_box):
            summa += B[i]
        for i in range(r_box*length_box, r+1):
            summa += A[i]
    return summa


if __name__ == "__main__":
    ans = input("Как Вы хочете ввести данные:\n1)Вручную \n2)Через файл\n")
    if ans == '1':
        try:
            A = [int(s) for s in input("Введи массив через пробел: ").split()]
            l = int(input("Введи левую границу: "))
            r = int(input("Введи правую границу: "))
            summa = sqrt_decomposition(A, l, r)
            print(summa)
        except:
            print("Вы некоректно ввели данные!")
    elif ans == '2':
        try:
            way = input("Введите путь к файлу: ")
            f = open(way,'r')
            A = [int(i) for i in f.readline().split()]
            l = int(f.readline())
            r = int(f.readline())
            summa = sqrt_decomposition(A, l, r)
            print(summa)
        except:
            print("В файле введены некоректно данные!")
    else:
        print("Домой")
