# Таможенные декларации ETGB
### Описание
В этом проекте реализован метод для получения таможенных деклараций Elektronik Ticaret Gümrük Beyannamesi (ETGB) для продавцов из Турции. Аналог метода из Ozon https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetEtgb
### Доступные эндпоинты и пример использования
- http://127.0.0.1:8000/api/v1/auth/signup/ (передаём в ключах "username", "email" свой логин и емаил. В ответ сервис присылает confirmation_code на указанный электронный адрес. Этот код можно найти в папке "send_emails")
- http://127.0.0.1:8000/api/v1/auth/authdata/ (передаём в ключах "username", "confirmation_code" свой логин и код подтверждения из прошлого ответа в ответ пользователю высылаются Client-Id, Api-Key которые необходимо внести в HEADER PARAMETERS)
- http://127.0.0.1:8000/api/v1/posting/global/etgb (получение таможенных деклараций ETGB за время указанное в ключах "from", "to". Если данные не переданы возвращается информация за период today() -4. Полученные декларации автоматически вносятся в вашу базу данных clickhouse. Для подключения сервиса к вашей базе данных необходимо создать файл ".env" и прописать ваши данные для подключения. Пример заполнения указан в файле ".env.example")
- Для удобного тестирования возможностей сервиса удаляю db.sqlite3 из gitignore и прикладываю данные для авторизации: Client-Id: 86965082774113484275972203771320
- http://127.0.0.1:8000/redoc/ - документация по апи
Api-Key: ODIrdttWd9xtoWNhLedAA49N3nr4QrUu
### Технологии
Python 3.9
Django 3.2
Django Rest Framework 3.12.4
clickhouse
SQLite3
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:OlegMusatov3000/Customs_declarations.git
```

```
cd customs_declarations
```

Cоздать виртуальное окружение:

```
python3.9 -m venv venv
```

Активировать виртуальное окружение:

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
Tg: @OlegMusatov
