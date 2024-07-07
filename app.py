from flask import Flask, flash
from flask import render_template, request, redirect, url_for
from project.events import NewlyWeds, Wedding
from project.users import Users

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

to_go = False ########

@app.route('/index')
@app.route('/', methods=['get', 'post'])
def index():
    client = ''

    client_name = ''
    client_mail = ''

    if request.method == 'POST':
        client_name = request.form.get("name")
        client_mail = request.form.get("email")
        print(client_mail, client_name)
        flash('Спасибо, будем ждать Вас на мероприятии!')
        return redirect(url_for('index'))

    return render_template('index.html',
                           client=client, user=Users(),
                           newl=NewlyWeds(), wed=Wedding())

@app.route('/<user>', methods=['get', 'post'])
def users_page(user):
    global to_go
    client = user

    client_name = ''
    client_mail = ''

    if request.method == 'POST':
        client_name = request.form.get("name")
        client_mail = request.form.get("email")
        to_go = True
        print(client_mail, client_name)
        flash('Спасибо, будем ждать Вас на мероприятии!')
        return redirect(f'/{client}')

    return render_template('index.html',
                           client=client, user=Users(), to_go=to_go,
                           newl=NewlyWeds(), wed=Wedding())

if __name__ == '__main__':
    app.run()