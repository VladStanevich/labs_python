import random
import string

def create_word(len):
    word = ''.join(random.choice(list(string.ascii_letters)) for x in range(len))
    return word

def create_line(len):
    str = ''
    for i in range(len):
        str += create_word(random.randint(i,10))
        str += ' '
    return str

print(create_line(5))