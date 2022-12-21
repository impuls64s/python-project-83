### Hexlet tests and linter status:
[![Actions Status](https://github.com/impuls64s/python-project-83/workflows/hexlet-check/badge.svg)](https://github.com/impuls64s/python-project-83/actions)
[![flake8 Lint](https://github.com/impuls64s/python-project-83/actions/workflows/lint.yml/badge.svg)](https://github.com/impuls64s/python-project-83/actions/workflows/lint.yml)

<p>Анализатор страниц - проверяет доступность сайта и записывает данные (ststus code, h1, title, description) в базу данных Postgresql. При разработке использовался <b>Flask</b> и <b>Poetry.</b></p>

<a target="_blank" href="https://imageban.ru/show/2022/12/20/14d7916f7fee0813bf8506096424f8ad/png"><img src="https://i1.imageban.ru/out/2022/12/20/14d7916f7fee0813bf8506096424f8ad.png" border="0" style='border: 1px solid #000000'></a>
<p>Для правильной работы необходимо созлать файл <b>.env</b> в корне проекта , и записать туда свои переменные окружения.</p>
<pre># У строки следующий формат: {provider}://{user}:{password}@{host}:{port}/{db}
DATABASE_URL = postgresql://user001:super_password@localhost:5432/page_analyz
SECRET_KEY = 'hobbit'</pre>
<p>Также для работы необходимо создать таблицы в базе данных, выполните код который находится в <b>database.sql</b></p>

<h2>Полезные команды</h2>

<pre><span class="pl-c"><span class="pl-c">#</span> install deps</span>
poetry install

<span class="pl-c"><span class="pl-c">#</span> run localy</span>
make dev

<span class="pl-c"><span class="pl-c">#</span> run at wsgi server</span>
make start</pre>
