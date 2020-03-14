import math

my_list = [int(s) for s in input("Введи элементы массива через пробел: ").split()]
number_box = math.ceil(math.sqrt(len(my_list)))
length_box = math.ceil(len(my_list) / number_box)
sum = [0]*number_box
for i in range(len(my_list)):
    sum[i//length_box] += my_list[i]
l = int(input("Введи левую границу: "))
r = int(input("Введи правую границу: "))
summa = 0
for i in range(len(sum)):
    if i <= l//3 or i >= r//3:
        continue
    else:
        summa += sum[i]
if l % length_box == 0:
    summa += sum[l//length_box]
else:
    for i in range(l, (l//length_box + 1)*length_box):
        summa += my_list[i]
if r % length_box == length_box - 1:
    summa += sum[r//length_box]
else:
    for i in range(r//length_box * length_box, r+1):
        summa += my_list[i]
print(summa)
