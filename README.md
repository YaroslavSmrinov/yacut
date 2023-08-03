YaCut - генератор которких ссылок.
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask-464646?style=flat&logo=Flask&logoColor=ffffff&color=043A6B)](https://flask-docs.readthedocs.io/en/latest/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=043A6B)](https://flask-docs.readthedocs.io/en/latest/)
[![Jinja2](https://img.shields.io/badge/-Jinja2-464646?style=flat&logo=Jinja&logoColor=ffffff&color=043A6B)](https://jinja.palletsprojects.com/en/2.10.x/intro/)

YaCut - учебный проект яндекс практикума. Проект генерирует сокращенную ссылку, сокращенная ссылка производит редирект по адресу, который был сокращен.
Длинная ссылка сохраняется в sqlite, в качестве ОРМ используется алхимия.
Есть веб интерфейс, есть 2 ручки:
* /api/id/ — POST на генерацию короткой ссылки;
* /api/id/<short_id>/ — GET на редирект на оригинальный адрес.

## Технологии
- Python 3.10
- Flask 2.0
- SQLAlchemy 1.4

## Установка

```
git clone git@github.com:YaroslavSmrinov/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip && pip install -r requirements.txt
```
Миграции алембика
```
flask db upgrade 
```
Запускайте
```
flask run
```
[Smirnov Iaroslav](https://t.me/irs_sm)

