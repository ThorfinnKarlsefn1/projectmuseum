#Сборка сайта 
import os
import json
import shutil
from flask import Flask, render_template

app = Flask(__name__)

# Загружаются данные c json-а.
with open('data.json', 'r', encoding='utf-8') as f:
    EXHIBITS = json.load(f)

# Создание папки под статический сайт.
os.makedirs('build', exist_ok=True)
os.makedirs('build/images', exist_ok=True)
os.makedirs('build/audio', exist_ok=True)
os.makedirs('build/qr', exist_ok=True)

# Копируем статические файлы
if os.path.exists('static/images'):
    shutil.copytree('static/images', 'build/images', dirs_exist_ok=True)
if os.path.exists('static/audio'):
    shutil.copytree('static/audio', 'build/audio', dirs_exist_ok=True)
if os.path.exists('static/qr'):
    shutil.copytree('static/qr', 'build/qr', dirs_exist_ok=True)
if os.path.exists('static/style.css'):
    shutil.copy('static/style.css', 'build/style.css')
if os.path.exists('static/script.js'):
    shutil.copy('static/script.js', 'build/script.js')

# Генерирация HTML-страницы
with app.app_context():
    # Главная страница
    html = render_template('index.html', exhibits=EXHIBITS)
    with open('build/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(" Создан index.html")

    # Страницы экспонатов
    for exp in EXHIBITS:
        html = render_template('exhibit.html', exhibit=exp)
        filename = f'build/exhibit_{exp["id"]}.html'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f" Создан exhibit_{exp['id']}.html")

print("\n Готово! Все файлы в папке build/")