#python main code for server . Пайтон мейн код для сервера
import json
import os
from flask import Flask, render_template, abort

app = Flask(__name__)

# Подгружаю данные с JSON-а при старте сервера
def load_exhibits():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

EXHIBITS = load_exhibits()


@app.route('/')
def index():
    #Главная страница на которой будет список всех экспонатов.
    return render_template('index.html', exhibits=EXHIBITS)


@app.route('/exhibit/<int:exhibit_id>')
def exhibit(exhibit_id):
    #Страница отдельного экспоната по его IDшнику.
    exhibit = next((e for e in EXHIBITS if e['id'] == exhibit_id), None)
    
    if not exhibit:
        abort(404)
    
    return render_template('exhibit.html', exhibit=exhibit)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('base.html', error='Экспонат не найден 😕 Возможно не тот QR-код.'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)