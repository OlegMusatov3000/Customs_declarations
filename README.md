# Таможенные декларации ETGB
### Описание
В этом проекте реализован метод для получения таможенных деклараций Elektronik Ticaret Gümrük Beyannamesi (ETGB) для продавцов из Турции. Аналог метода из Ozon https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetEtgb
### Доступные эндпоинты и пример использования
- http://127.0.0.1:8000/api/v1/api-token-auth/ (передаём логин и пароль, получаем токен)
- http://127.0.0.1:8000/api/v1/api-token-auth/ (передаём логин и пароль, получаем токен)
- http://127.0.0.1:8000/api/v1/posting/global/etgb (получение таможенных деклараций ETGB)
- пример использования 
### Технологии
Python 3.9
Django 2.2.19
Django Rest Framework 3.12.4
Simple JWT
SQLite3
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:OlegMusatov3000/customs_declarations.git
```

```
cd customs_declarations
```

Cоздать и активировать виртуальное окружение:

```
python3.9 -m venv venv
```

Команда для Windows:

```
source venv/Scripts/activate
```

Для Linux и macOS:

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Автор
Олег Мусатов
