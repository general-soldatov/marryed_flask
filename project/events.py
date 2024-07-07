from datetime import date
from math import sin

class Wedding:
    def __init__(self):
        self.up_case = [
            ['Home', '/index'],
            ['Telegram-канал', 'https://t.me/+WPAfW9tNMKE4M2Fi'],
            ['Цветочная подписка', '#']
        ]
        self.events = [
            ['Welcome', 'images/welcome.jpg', '16:00 - 17:00', 'Время пролетит незаметно за общением с другими гостями. Кроме того, ожидание скрасит приветственный фуршет и бокал игристого.'],
            ['Выездная регистрация', 'images/wedding.jpg', '17:00 - 18:00', 'Здесь начинается семья.'],
            ['Свадебный ужин', 'images/dinner.jpg', '18:00 - 22:00', 'Такое событие, что не отметить непростительно!']
        ]
        self.family = [
            ['Игорь Солдатов', 'папа', 'vk', '#', 'images/couple-1.jpg', 'spitch'],
            ['Любовь Солдатова', 'мама', 'vk', '#', 'images/couple-2.jpg', 'spitch'],
            ['Виктор Малюгин', 'папа', 'vk', '#', 'images/couple-3.jpg', 'spitch'],
            ['Анна Малюгина', 'мама', 'vk', '#', 'images/couple-1.jpg', 'spitch'],
            ['Валерия Малюгина', 'сестра', 'vk', '#', 'images/couple-2.jpg', 'spitch']
        ]
        self.calendar = ['Wedding+Soldatov`s', '20240811T130000', '20240811T190000', 'https://example.com/tickets-43251101208', 'Studio 12. 24']

        self.date = '11 августа 2024 год'
        self.week_day = 'Воскресенье'
        self.location = 'с. Новая Усмань, Усадьба 12.24'

class NewlyWeds:
    def __init__(self):
        self.about = [
            ['Юрий Солдатов', 'images/yura.jpeg', 'От студенческой скамьи до преподавательской кафедры.'],
            ['Эльвира Малюгина', 'images/elya.jpeg', 'Никто не знает о здоровье больше, чем она.']
        ]
        self.together_day = self.together()
        self.time_kiss = self.kiss()

    def together(self):
        start = date(2022, 9, 23)
        now = date.today()
        return (now - start).days

    def kiss(self):
        return int((sin(self.together()) + 3)*65.3)