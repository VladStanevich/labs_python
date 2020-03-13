import random
import string

def create_word(len):
    word = ''.join(random.choice(list(string.ascii_letters)) for x in range(len))
    return word

for i in range(10):
    print(create_word(random.randint(3,10)))