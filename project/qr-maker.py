from os import getcwd
import qrcode
from PIL import Image, ImageDraw, ImageFont

def procedure(hyper, name):
    global back
    img = qrcode.make(hyper)
    font = ImageFont.truetype('C:/Users/Юрий Солдатов/PycharmProjects/married_flask/marryed_flask/project/monotypecorsiva.ttf', size=40)
    font_hyper = ImageFont.truetype('C:/Windows/Fonts/GARA.TTF', size=33)

    def center_text(text, font_text, y):
        text_size = font_text.font.getsize(text)[0]
        text_name = ImageDraw.Draw(back)
        text_name.text(
            xy=((back.size[0] - text_size[0]) // 2, y),
            text=text,
            font=font_text,
            fill=(0, 0, 0)
        )


    if len(name) > 25:
        txt = name.split(sep=' ')
        n = len(txt) // 2
        name1 = ' '.join(txt[:n+1])
        name2 = ' '.join(txt[n+1:])
        back.paste(img, (60, 90))
        center_text(name1, font, 20)
        center_text(name2, font, 70)
        center_text(hyper, font_hyper, 450)

    else:
        back.paste(img, (60, 60))
        center_text(name, font, 20)
        center_text(hyper, font_hyper, 430)

    # back.show()

hypers = 'https://юра-и-эля.рф/15gk8f9d'
names = 'Георгий Николаевич и Антонина Сергеевна'

mypath = '/static/base/adress.txt'

with open(getcwd()+mypath, 'r', encoding='utf-8') as adress:
    for i, item in enumerate(adress, 1):
        back = Image.new('RGB', (500, 500), color=(255, 255, 255))
        line = item.strip().split(sep=' | ')
        procedure(line[1], line[0])
        back.save(f'image_{i}.png')

    print('success')
