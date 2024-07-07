from flask import Flask, flash
from flask import render_template, request, redirect, url_for
from project.events import NewlyWeds, Wedding
from project.users import Users, User

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/index')
@app.route('/')
def index():
    client = False

    client_name = ''
    client_mail = ''

    if request.method == 'POST':
        client_name = request.form.get("phone")
        client_mail = request.form.get("email")
        print(client_mail, client_name)
        flash('Спасибо, будем ждать Вас на мероприятии!')
        return redirect(url_for('index'))

    return render_template('index.html',
                           client=client, user=Users(),
                           newl=NewlyWeds(), wed=Wedding())

@app.route('/<user>', methods=['get', 'post'])
def users_page(user):
    path = url_for('static', filename='base/guests.txt')
    togo_base = url_for('static', filename='base/togo.txt')

    user_source = User(user, path, togo_base)
    client = user_source.to_go
    to_go = user_source.go()

    client_phone = ''
    client_mail = ''

    if request.method == 'POST':
        client_phone = request.form.get("phone")
        client_mail = request.form.get("email")
        user_source.go_add(client_mail, client_phone)
        flash('Спасибо, будем ждать Вас на мероприятии!')
        return redirect(f'/{user}')

    return render_template('index.html',
                           client=client, user=Users(), to_go=to_go,
                           newl=NewlyWeds(), wed=Wedding())

if __name__ == '__main__':
    app.run()