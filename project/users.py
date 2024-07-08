from os import getcwd

class User:
    def __init__(self, ids, path, togo_base):
        self.path = getcwd() + path
        self.togo_base = getcwd() + togo_base
        self.ids = ids
        self.gender = 'm'
        self.name = ''
        self.guest = 0
        self.waiting = 0

        self.to_go = self.base()

    def base(self):
        with open(self.path, 'r', encoding='utf-8') as text:
            flag = False
            for item in text:
                txt = item.strip().split(sep='/ ')
                self.waiting += int(txt[2])
                if txt[1] == self.ids:
                    self.gender = txt[0]
                    self.guest = txt[2]
                    self.name = ''.join(txt[3:])
                    flag = True
        return flag

    def go_add(self, *args):
        line = [self.ids, self.guest]
        line.extend(args)
        line.append(self.name)
        with open(self.togo_base, 'a', encoding='utf-8') as file:
            file.write(', '.join(line) + '\n')

    def go(self):
        with open(self.togo_base, 'r', encoding='utf-8') as text:
            for item in text:
                tst = item.strip().split(sep=', ')
                if self.ids == tst[0]:
                    return True
        return False

    def come_event(self):
        gos = 0
        with open(self.togo_base, 'r', encoding='utf-8') as text:
            for item in text:
                tst = item.strip().split(sep=', ')
                gos += tst[1]


class Users(User):

    def go_event(self):
        gos = 0
        with open(self.togo_base, 'r', encoding='utf-8') as text:
            for item in text:
                tst = item.strip().split(sep=', ')
                gos += int(tst[1])

            return gos

    def welcome(self):
        if self.gender == 'm':
            text = 'Дорогой'
        elif self.gender == 'f':
            text = 'Дорогая'
        elif self.gender == 'p':
            text = 'Дорогие'
        else:
            return 'Привет!'

        return f'{text} {self.name}!'

    def question(self):
        if self.gender == 'p':
            return f'{self.name}, вы придёте?'
        elif self.gender in ['f', 'm']:
            return f'{self.name}, Вы придёте?'
        else:
            return 'Вы придёте?'

    def appeal(self):
        return self.gender in ['f', 'm']
