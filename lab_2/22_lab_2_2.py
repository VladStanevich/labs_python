import random
import string
import os.path

def create_word(len):
    word = ''.join(random.choice(list(string.ascii_letters)) for x in range(len))
    return word

def create_file(size, K=(10,100), L=(3,10)):
    f = open("lab_2/output.txt", "w")
    sz = os.path.getsize("lab_2/output.txt")
    while sz < size:
        stroka = random.randint(*K)
        for i in range(stroka):
            f.write(create_word(random.randint(*L)))
            sz = os.path.getsize("lab_2/output.txt")
            if sz >= size:
                break
            if i == stroka-1:
                f.write("\n")
            else:
                f.write(" ") 
    f.close()


if __name__ == "__main__":
    create_file(1024)
