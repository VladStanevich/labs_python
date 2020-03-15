import random
import string
import os.path

def create_word(len):
    word = ''.join(random.choice(list(string.ascii_letters)) for x in range(len))
    return word

def create_line(len):
    stroka = ''
    for x in range(len):
        stroka += create_word(random.randint(3,10))
        stroka += ' '
    return stroka

def create_file(size):
    f = open("output.txt", "w")
    sz = os.path.getsize("output.txt")
    while sz < size:
        f.write(create_line(random.randint(10,100))+"\n")
        sz = os.path.getsize("output.txt")
    f.close()


if __name__ == "__main__":
    create_file(1024**2)
