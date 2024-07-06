from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    weddind_date = '11 августа 2024 год'
    week_day = 'Воскресенье'
    location = 'с. Новая Усмань, Усадьба 12.24'
    go_to = 10
    waiting = 50
    together_day = 100
    time_kiss = 100

    up_case = [
        ['Home', 'index.html'],
        ['Telegram-канал', '#'],
        ['Цветочная подписка', '#']
    ]
    newlyweds = [
        ['Юрий Солдатов', 'images/yura.jpeg', 'От студенческой скамьи до преподавательской кафедры.'],
        ['Эльвира Малюгина', 'images/elya.jpeg', 'Никто не знает о здоровье больше, чем она.']
    ]
    events = [
        ['Welcome', 'images/welcome.jpg', '16:00 - 17:00', 'Здесь Вы сможете познакомиться с гостями.'],
        ['Выездная регистрация', 'images/wedding.jpg', '17:00 - 18:00', 'Здесь начинается семья.'],
        ['Свадебный ужин', 'images/dinner.jpg', '18:00 - 22:00', 'Такое событие, что не отметить непростительно!']
    ]
    family = [
        ['Игорь Солдатов', 'папа', 'vk', '#', 'images/couple-1.jpg', 'spitch'],
        ['Любовь Солдатова', 'мама', 'vk', '#', 'images/couple-2.jpg', 'spitch'],
        ['Виктор Малюгин', 'папа', 'vk', '#', 'images/couple-3.jpg', 'spitch'],
        ['Анна Малюгина', 'мама', 'vk', '#', 'images/couple-1.jpg', 'spitch'],
        ['Валерия Малюгина', 'сестра', 'vk', '#', 'images/couple-2.jpg', 'spitch']
    ]
    calendar = ['Wedding+Soldatov`s', '20240811T130000', '20240811T190000', 'https://example.com/tickets-43251101208', 'Studio 12. 24']
    return render_template('index.html',
                           date=weddind_date, week_day=week_day,
                           go_to = go_to, waiting=waiting,
                           together_day=together_day, time_kiss=time_kiss,
                           family=family, up_case=up_case, cal=calendar,
                           location=location, newlyweds=newlyweds, events=events)

if __name__ == '__main__':
    app.run()