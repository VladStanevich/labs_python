import random
import string
import os.path

def create_word(len):
    word = ''.join(random.choice(list(string.ascii_letters)) for x in range(len))
    return word

def create_line(len):
    stroka = ''
    for i in range(len):
        stroka += create_word(random.randint(3,10))
        stroka += ' '
    return stroka

f = open("output.txt", "w")
size = os.path.getsize("output.txt")
while size < 1024:
    f.write(create_line(random.randint(10,100))+"\n")
    size = os.path.getsize("output.txt")
f.close()
