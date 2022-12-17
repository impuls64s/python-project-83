from flask import Flask, render_template, request, flash, get_flashed_messages, url_for, redirect
from .creator import add_to_database, data_url, data_all, check_in_db, add_to_url_checks, data_all_url_checks, data_all_all_site
import validators
import os
from urllib.parse import urlparse


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def home():
    return render_template('index.html')


@app.post('/urls')
def url_add():
    name_url = request.form.get('url')
    if validators.url(name_url, public=True) and len(name_url) < 255:
        a = urlparse(name_url)
        normalize_url = (f"{a.scheme}://{a.hostname}")
        
        if check_in_db(normalize_url):
            flash('Страница уже существует', 'info')
            iid = list(check_in_db(normalize_url))
            return redirect(url_for('url_id', id=str(iid[0])))
        
        new_data = list(add_to_database(normalize_url))
        flash('Страница успешно добавлена', 'success')
        return redirect(url_for('url_id', id=str(new_data[0])))
    
    flash('Некорректный URL', 'error')
    messages = get_flashed_messages(with_categories=True)
    return render_template('index.html',  messages=messages, data=name_url)


@app.get('/urls')
def get_urls():
    #data = list(data_all())
    data_all_site = list(data_all_all_site())
    return render_template('all_site.html', data_all_site=data_all_site)


@app.route('/urls/<id>')
def url_id(id):
    messages = get_flashed_messages(with_categories=True)
    data = list(data_url(id))
    data_checks = list(data_all_url_checks(id))
    return render_template('item.html', data=data, messages=messages, data_checks=data_checks)


# добавления в таблицу url_cheks нового id и возврат всех данных где id = id функции
@app.post('/urls/<id>/checks')
def checks(id):
    add_to_url_checks(id)
    flash('Страница успешно проверена', 'success')
    return redirect(url_for('url_id', id=id))
