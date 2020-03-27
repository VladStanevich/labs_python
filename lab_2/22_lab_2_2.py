import random
import string
import os.path


def create_word(len):
    word = ''.join(random.choice(list(string.ascii_letters)) for x in range(len))
    return word

def create_file(size, K=(10,100), L=(3,10)):
    sz = 0
    size *= 1024**2
    f = open("lab_2/output.txt", 'w')
    f.seek(0)
    f.close() 
    while sz < size:
        stroka = random.randint(*K)
        f = open("lab_2/output.txt", 'a') 
        for i in range(stroka):
            f.write(create_word(random.randint(*L)))
            if i == (stroka - 1):
                f.write("\n")
            else:
                f.write(" ")
        f.close()
        sz = os.path.getsize("lab_2/output.txt")
        print("{} %".format(sz*100//size))
    print("Complited!")


if __name__ == "__main__":
    create_file(1)
