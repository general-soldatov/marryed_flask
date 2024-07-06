from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    weddind_date = '11 августа 2024 год'
    week_day = 'Воскресенье'
    return render_template('index.html', date=weddind_date, week_day=week_day)

if __name__ == '__main__':
    app.run()