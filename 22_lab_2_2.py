import random
import string

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
f.write(create_line(150))
f.close()