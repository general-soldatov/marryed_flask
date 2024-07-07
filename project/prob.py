from random import randint, choice
from string import ascii_lowercase, digits

mypath = 'C:/Users/Юрий Солдатов/PycharmProjects/married_flask/marryed_flask/project/guests.txt'


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
    codes = []
    with open(path, 'r', encoding='utf-8') as text:
        for item in text:
            txt = item.strip().split(sep=', ')[1]
            codes.append(txt)

        print(codes)

# codeSafe(mypath)
codeAdress(mypath)