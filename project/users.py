from os import getcwd

class Users:
    def __init__(self):
        self.go_to = 10
        self.waiting = 50


class User:
    def __init__(self, ids, path, togo_base):
        self.path = getcwd() + path
        self.togo_base = getcwd() + togo_base
        self.ids = ids
        self.gender = 'm'
        self.name = ''
        self.waiting = 0
        self.guest = 0

        self.to_go = self.base()

    def base(self):
        with open(self.path, 'r', encoding='utf-8') as text:
            flag = False
            for item in text:
                txt = item.strip().split(sep=', ')
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
        with open(self.togo_base, 'a') as file:
            file.write(', '.join(line) + '\n')

    def go(self):
        with open(self.togo_base, 'r') as text:
            for item in text:
                tst = item.strip().split(sep=', ')
                if self.ids == tst[0]:
                    return True

        return False

    def come_event(self):
        self.waiting = 0
        with open(self.togo_base, 'r') as text:
            for item in text:
                tst = item.strip().split(sep=', ')
                self.waiting += tst[1]