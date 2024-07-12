from random import randint, choice
from string import ascii_lowercase, digits
from os import getcwd

mypath = '/static/base/guests.txt'


def codeSafe(paths):
    '''Скрипт присвоения индивидуальных кодов в реферальную ссылку
    '''
    char = [ascii_lowercase, digits]
    codes = []
    with open(paths, 'r', encoding='utf-8') as text:
        for item in text:
            line = item.strip() + ', ' + ''.join([choice(char[randint(0, 1)]) for _ in range(8)])
            codes.append(line)

    with open(paths, 'w', encoding='utf-8') as text:
        for item in codes:
            text.write(item + '\n')

def codeAdress(path):
    mypath = '/static/base/adress.txt'
    codes = []
    with open(getcwd() + path, 'r', encoding='utf-8') as text:
        for item in text:
            txt = item.strip().split(sep='/ ')
            codes.append(f'{txt[3]} | https://юра-и-эля.рф/{txt[1]}\n')

    with open(getcwd() + mypath, 'w', encoding='utf-8') as text:
        for item in codes:
            text.writelines(item)

# codeSafe(mypath)
codeAdress(mypath)